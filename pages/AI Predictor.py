import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import cv2 
import uuid
import numpy as np
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
# Page config
# st.set_page_config(page_title="Facial Recognition", page_icon="📊")


fb_credentials = {"type": st.secrets.firebase["type"],
  "project_id": st.secrets.firebase["project_id"],
  "private_key_id": st.secrets.firebase["private_key_id"],
  "private_key": st.secrets.firebase["private_key"],
  "client_email": st.secrets.firebase["client_email"],
  "client_id": st.secrets.firebase["client_id"],
  "auth_uri": st.secrets.firebase["auth_uri"],
  "token_uri": st.secrets.firebase["token_uri"],
  "auth_provider_x509_cert_url": st.secrets.firebase["auth_provider_x509_cert_url"],
  "client_x509_cert_url": st.secrets.firebase["client_x509_cert_url"],
  "universe_domain": st.secrets.firebase["universe_domain"]
}

# Use a service account.
cred = credentials.Certificate(fb_credentials)
# app = firebase_admin.initialize_app(cred)
try:
    firebase_admin.get_app()
except ValueError as e:
    firebase_admin.initialize_app(cred)
db = firestore.client()

# Configure page settings
st.set_page_config(
    page_title="Welcome",
    page_icon="✨",
    layout="wide",
    # initial_sidebar_state="collapsed",
   
)

if 'gender' not in st.session_state:
    st.session_state.submitted = False
    st.session_state.gender = ""
    st.session_state.age = ""
    st.session_state.pred_gender = ""
    st.session_state.pred_age = ""
    st.session_state.race = ""
    st.session_state.gender_result = False
    st.session_state.age_result = False

# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def submit():
    st.session_state.submitted = True
    doc_ref = db.collection("question2").document(str(uuid.uuid4()))
    doc_ref.set({"answer" : [st.session_state.race, st.session_state.gender, st.session_state.gender_result, st.session_state.age_result]})
                 
# Load custom CSS
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.markdown("""
    <div class="header-container">
        <h1>Facial Recognition</h1>
        <p style="text-align:center; font-size: 1.35rem;">Interactive Demo</p>
    </div>
""", unsafe_allow_html=True)

def render_header():
    """Render the app header"""
    st.title("📊 Real-time Age & Gender Predictor")
    st.markdown("""
    This app uses your webcam to predict age and gender in real-time.
    The predictions are made using deep learning models
    """)

def render_instructions():
    """Render usage instructions"""
    with st.expander("ℹ️ Instructions", expanded=False):
        st.markdown("""
        ### How to use:
        1. Grant camera permissions when prompted
        2. Position your face in the center of the frame
        3. Ensure good lighting for better predictions
        4. The predictions will appear at the bottom of the video feed
        
        ### Notes:
        - Try with different facial expressions 
        - Try with different face views
        """)

   
def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn=frame.copy()
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections=net.forward()
    faceBoxes=[]
    for i in range(detections.shape[2]):
        confidence=detections[0,0,i,2]
        if confidence>conf_threshold:
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            faceBoxes.append([x1,y1,x2,y2])
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    return frameOpencvDnn,faceBoxes


tab1, tab2, tab3, tab4 = st.tabs(["Live Demo", "Demographic Comparison", "Classroom Exercise", "Classroom Results"])
    
with tab2:
    st.header("Comparative Analysis")
    st.write("""
    Explore how facial recognition accuracy varies across different demographic groups.
    This analysis helps demonstrate potential biases in AI systems.
    """)
    df = pd.read_csv("fairface_results.txt")
    st.bar_chart(df, x="race", y="gender", stack=False, color='#9370DB', horizontal=True)
    st.bar_chart(df, x="race", y="age", stack=False, color='#DDA0DD', horizontal=True)
          
    st.subheader("Key Points to Notice:")
    st.markdown("""
    - Detection accuracy for age and gender varies across different demographics
    - Confidence scores may differ based on lighting and pose
    """)
  
    st.bar_chart(df, x="race", y="participants", stack=False, color='#DAA520', horizontal=True)
  

with tab3:
    st.header("But the question is:")
    st.markdown("### How good is the model for the people in this room?")
    st.write("""
    We saw how the demo was for the group of some random participants from a curated dataset. The real question is, how did it perform for you?
    """)
     
    # Feedback form
    col1, col2 = st.columns(2)
    with col1:
        gender_map_options = { "Female": ":material/female:",   "Male": ":material/male:", "Other": ":material/transgender:"} 
        st.markdown("#### Your actual gender:")
        user_gender = st.segmented_control(
            "actual_gender",
            options=gender_map_options.keys(),
            format_func=lambda option: gender_map_options[option],
            label_visibility="collapsed",
            key="gt"
        )
    # pred_gender_map_options = { "Female": ":material/female:",   "Male": ":material/male:", "Other": ":material/transgender:"} 
    with col2:
        st.markdown("#### Model's prediction:")
        model_gender = st.segmented_control(
            "predicted_gender",
            options=gender_map_options.keys(),
            format_func=lambda option: gender_map_options[option],
            label_visibility="collapsed",
            key="pred"
        )

    st.session_state.gender = user_gender
    st.session_state.pred_gender = model_gender

    st.markdown("---")
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("#### Your actual age group:")
        user_age = st.segmented_control(
            "actual_age",
            options=["0-2", "4-6", "8-12", "15-20", "25-32", "38-43", "48-53", "53+"],
            label_visibility="collapsed",
            key="gt_age"
           
        )
    with col4:
        st.markdown("#### Model's prediction:")
        model_age = st.segmented_control(
            "predicted_age",
            options=["0-2", "4-6", "8-12", "15-20", "25-32", "38-43", "48-53", "53+"],
            label_visibility="collapsed",
            key="pred_age_res"
        )
    st.session_state.age = user_age
    st.session_state.pred_age = model_age
    st.markdown("---")
    race_options = ["Asian", "Black", "Hispanic", "White", "Other"]
    user_race = st.segmented_control("race", options=race_options)


    st.session_state.race = user_race
    st.session_state.gender_result = int(user_gender==model_gender)
    st.session_state.age_result = int(user_age==model_age)
    if st.button("Submit Feedback", on_click=submit):
        st.success("Thank you for your feedback! Now let's have a look at everyone's results!")

    with tab4:
      
      
      answers = db.collection("question2")
      docs = answers.stream()
      df = pd.DataFrame()
      r = []
      filter_by = { 0: "Gender Prediction Results",   1: "Age Prediction Results"} 

      for doc in docs: 
        r.append(doc.to_dict()["answer"])
      df = pd.DataFrame(r, columns=["race", "gender", "gender results", "age results"])

              # Create heatmap for selected metric

      st.subheader("Results")
      st.markdown("Hopefully it's clear by now that AI research depends *lots and lots (and lots)* of data and testing ")
      st.markdown("Technically we just ran a little experiment to see how good this model was with a sample of participants (that's you, the students!). Now let's analyze the results and see if we can make any conclusions about our AI! ")
      
      col1, col2 = st.columns(2)
      with col1: 
        # Bar chart by gender
        fig_gen = px.bar(
            df.groupby(['race', 'gender'])['gender results'].mean().reset_index(),
            x='race',
            y='gender results',
            title="Average Accuracy by Gender and race",
            color='gender'
        )
        st.plotly_chart(fig_gen, use_container_width=True)

      with col2:

        fig_age = px.bar(
            df.groupby(['race', 'gender'])['age results'].mean().reset_index(),
            x='race',
            y='age results',
            title=f"Average Accuracy by age and race",
            color='gender'
        )
        st.plotly_chart(fig_age, use_container_width=True)
        
          
        
      st.markdown("""
      - The first figure tells us how good our AI was at predicting the gender for each group of people. 
      - The second figure tells us how good our AI was at predicting the age for each race group. 
      - The higher the bars, the better the performance. The colors tell us about the gender of the participants. What do you notice?
      """)
      
      st.subheader("Cooler charts")
      st.markdown("We don't only deal with bar charts, especially when the data becomes more complex.")
      st.markdown("Let's have another view of the data and see if we are able to notice anything else!")
      
      col11, col22 = st.columns(2)
      with col11: 
        fig_box = px.box(
            df.groupby(['race', 'gender'])['gender results'].mean().reset_index(),
            x='race',
            y='gender results',
            color='gender',
            title="Accuracy Distribution by Demographics",
            points="all"
        )
        st.plotly_chart(fig_box, use_container_width=True)

      with col22:
        fig_heatmap = px.density_heatmap(
            df.groupby(['race', 'gender'])['age results'].mean().reset_index(),
            x='gender', 
            y='race', 
            z='age results',
            title="Accuracy Heatmap",
            color_continuous_scale='RdBu_r'
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)


      st.markdown("""
      - The first figure summarizes the performance of the model at predicting the gender for each category of people. For example: While females are grouped together, black males are group together, etc. 
      - The second figure is called a heatmap and it also summarizes how good our AI was at predicting the age for each group. 
      - Do you notice anything new from these figures?
      """)  
      # st.subheader("Finally, how good was the model at predicting your genders?")
      # df1 = df.groupby('race')['gender results'].mean().reset_index(drop=True)
      # st.dataframe(df1, use_container_width=True)
      # # df1['age results'].to_frame().style.format('{:,.3f}%')
      # # st.dataframe(df1, use_container_width=True)

      # st.subheader("What about your ages?")

      # df2 = df.groupby('race')['age results'].mean().reset_index(drop=True)
      # df2['gender results'].to_frame().style.format('{:,.3f}%')
      # st.dataframe(df2, use_container_width=True)
      # st.markdown("### Gender Prediction Results")
      # st.scatter_chart(df, x="race", y="gender", y_label="Gender: Female/Male/Other", color="gender results", size=100)
      # st.markdown("### Race Prediction Results")
      # st.scatter_chart(df, x="race", y="gender", y_label="Gender: Female/Male/Other", color="age results", size=100)
            
        
    # st.subheader("Key Points to Notice:")
    # st.markdown("""
    # - Detection accuracy varies across different demographics
    # - Confidence scores may differ based on lighting and pose
    # - The system provides basic demographic estimates
    # """)
    
    # st.subheader("Analyzing the Comparison:")
    # st.markdown("""
    # - Detection Rate: How often the system successfully identifies a face
    # - Confidence Score: How sure the system is about its predictions
    # - Accuracy Variations: Patterns in performance across groups
    # """)


with tab1: 
    render_header()
    render_instructions()


    faceProto="opencv_face_detector.pbtxt"
    faceModel="opencv_face_detector_uint8.pb"
    ageProto="age_deploy.prototxt"
    ageModel="age_net.caffemodel"
    genderProto="gender_deploy.prototxt"
    genderModel="gender_net.caffemodel"

    MODEL_MEAN_VALUES=(78.4263377603, 87.7689143744, 114.895847746)
    # ageList=['(0-2)', '(2-4)', '(4-6)', '(6-8)', '(8-12)', '(12-15)', '(15-20)',  '(20-25)','(25-32)', '(32-38)','(38-43)', '(43-48)', '(48-53)', '(53-60)', '(60-100)']
    ageList=['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']

    genderList=['Male','Female']

    faceNet=cv2.dnn.readNet(faceModel,faceProto)
    ageNet=cv2.dnn.readNet(ageModel,ageProto)
    genderNet=cv2.dnn.readNet(genderModel,genderProto)

    # video=cv2.VideoCapture(args.image if args.image else 0)
    # padding=20

    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        # Check the type of cv2_img:
        # Should output: <class 'numpy.ndarray'>
        # st.write(type(cv2_img))

        # Check the shape of cv2_img:
        # Should output shape: (height, width, channels)
        # st.write(cv2_img.shape)
        padding=20
        frame = cv2_img
        resultImg,faceBoxes=highlightFace(faceNet,frame)
        if not faceBoxes:
            st.write("No face detected")
        for faceBox in faceBoxes:
            face=frame[max(0,faceBox[1]-padding):
                        min(faceBox[3]+padding,frame.shape[0]-1),max(0,faceBox[0]-padding)
                        :min(faceBox[2]+padding, frame.shape[1]-1)]

            blob=cv2.dnn.blobFromImage(face, 1.0, (227,227), MODEL_MEAN_VALUES, swapRB=False)
            genderNet.setInput(blob)
            genderPreds=genderNet.forward()
            gender=genderList[genderPreds[0].argmax()]
           # st.write(f'Gender: {genderPreds[0]}')

            ageNet.setInput(blob)
            agePreds=ageNet.forward()
            age=ageList[agePreds[0].argmax()]
            # st.write(f'Age: {age[1:-1]} years')
            with st.expander("🚩Results", expanded=False):
                st.write(f"Gender: {gender}")
                st.write(f"Age: {age[1:-1]} years")
                cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
                st.image(resultImg)

            with st.expander("👁️ Under the hood", expanded=False):
                # st.write(type(agePreds[0]))
                # st.write(str(agePreds[0]).split(" "))
                st.markdown(f"""How did the model figure out the gender? Well, it didn't. 
                            From the data it has seen before, it calculated the probabilities below:
                    """)
                genders = [genderPreds[0][0], genderPreds[0][1]]
                df1 = pd.DataFrame(pd.DataFrame(genders).T.values, columns=["Male", "Female"])
                st.bar_chart(genderPreds[0], y_label="Gender", x_label="Probability", horizontal=True, stack=True)

                ages = []
                for element in agePreds[0]: 
                    ages.append(element)
            
                df2 = pd.DataFrame(pd.DataFrame(ages).T.values, columns=ageList)
                st.bar_chart(df2, y_label="Age Range", x_label="Probability", horizontal=True)

                #st.write(f"Age: {age[1:-1]} years")
                #cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,255), 2, cv2.LINE_AA)
                #st.image(resultImg)

    # # while cv2.waitKey(1)<0 :
    # #     hasFrame,frame=video.read()
    # #     if not hasFrame:
    # #         cv2.waitKey()
    # #         break

    #
