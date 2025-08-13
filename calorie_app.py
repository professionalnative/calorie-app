gender = st.selectbox('Gender', ['male', 'female']) # a dropdown
age = st.slider('Age', 10, 100, 25) # using a slider
height = st.number_input('Height', 100, 250, 170) # to enter the value manually
weight = st.number_input('Weight (kg)', 30, 200, 70)
duration = st.slider('Exercise Duration (min)', 1, 180, 30)
heart_rate = st.slider('Heart Rate', 60, 200, 100)
body_temp = st.slider('Body Temperature (Celsius)', 35.0, 45.0, 37.0)

# compute the BMI
bmi = weight/(height/100) ** 2

# predict button

if st.button('predict calorie burned'):
  data = {
      'Gender': [gender],
      'Age': [age],
      'Height': [height],
      'Weight': [weight],
      'Duration': [duration],
      'Heart_Rate': [heart_rate],
      'Body_Temp': [body_temp],
      'BMI': [bmi]
  }
  # create a dataframe
  df = pd.DataFrame(data)

  # load the saved model
  model = joblib.load('calorie_predictor.pkl')

  # predict our model
  calorie = model.predict(df)

  st.success(f'Estimated Calorie Burned: {calorie[0]:.2f} kcal')
