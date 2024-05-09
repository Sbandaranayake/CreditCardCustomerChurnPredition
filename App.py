import streamlit as st
import pickle

# Load the Random Forest Classifier model
with open('Credit_Card_Customer_Churn_Prediction.pkl', 'rb') as file:
    model = pickle.load(file)

# Function to make predictions
def predict_churn(input_data):
    prediction = model.predict(input_data)
    return prediction

# Streamlit app
def main():
    st.markdown('<h1 style="text-align: center; color: blue; margin-bottom:40px;">Customer Churn Prediction</h1>', unsafe_allow_html=True)

    # Input fields
    customer_age = st.number_input('Customer Age', min_value=18, max_value=100, value=30)
    gender = st.selectbox('Gender', ['Male', 'Female'])
    dependent_count = st.number_input('Dependent Count', min_value=0, max_value=10, value=0)
    income_category = st.selectbox('Income Category', ['Less than $40K', '$40K - $60K', '$60K - $80K', '$80K - $120K', '$120K +'])
    months_on_book = st.number_input('Months on Book', min_value=0, max_value=100, value=0)
    total_relationship_count = st.number_input('Total Relationship Count', min_value=0, max_value=10, value=0)
    months_inactive_12_mon = st.number_input('Months Inactive (12 months)', min_value=0, max_value=12, value=0)
    contacts_count_12_mon = st.number_input('Contacts Count (12 months)', min_value=0, max_value=20, value=0)
    credit_limit = st.number_input('Credit Limit', min_value=0, max_value=100000, value=0)
    total_revolving_bal = st.number_input('Total Revolving Balance', min_value=0, max_value=100000, value=0)
    avg_open_to_buy = st.number_input('Average Open to Buy', min_value=0, max_value=100000, value=0)
    total_amt_chng_q4_q1 = st.number_input('Total Amount Change (Q4 - Q1)', min_value=0.0, max_value=10.0, value=0.0, step=0.01)
    total_trans_amt = st.number_input('Total Transaction Amount', min_value=0, max_value=100000, value=0)
    total_trans_ct = st.number_input('Total Transaction Count', min_value=0, max_value=100, value=0)
    total_ct_chng_q4_q1 = st.number_input('Total Count Change (Q4 - Q1)', min_value=0.0, max_value=10.0, value=0.0, step=0.01)
    avg_utilization_ratio = st.number_input('Average Utilization Ratio', min_value=0.0, max_value=1.0, value=0.0, step=0.01)
    education_level_college = st.number_input('Education Level College', min_value=0, max_value=1, value=0)
    education_level_graduate = st.number_input('Education Level Graduate', min_value=0, max_value=1, value=0)
    education_level_high_school = st.number_input('Education Level High School', min_value=0, max_value=1, value=0)
    education_level_other = st.number_input('Education Level Other', min_value=0, max_value=1, value=0)
    education_level_uneducated = st.number_input('Education Level Uneducated', min_value=0, max_value=1, value=0)
    divorced = st.number_input('Divorced', min_value=0, max_value=1, value=0)
    married = st.number_input('Married', min_value=0, max_value=1, value=0)
    single = st.number_input('Single', min_value=0, max_value=1, value=0)
    card_category_blue = st.number_input('Card Category Blue', min_value=0, max_value=1, value=0)
    card_category_gold = st.number_input('Card Category Gold', min_value=0, max_value=1, value=0)
    card_category_platinum = st.number_input('Card Category Platinum', min_value=0, max_value=1, value=0)
    card_category_silver = st.number_input('Card Category Silver', min_value=0, max_value=1, value=0)

    # Preprocess input data
    gender_mapping = {'Male': 0, 'Female': 1}
    income_mapping = {'Less than $40K': 0, '$40K - $60K': 1, '$60K - $80K': 2, '$80K - $120K': 3, '$120K +': 4}
    education_mapping = {'High School': 0, 'Graduate': 1, 'Uneducated': 2, 'College': 3, 'Post-Graduate': 4, 'Doctorate': 5}
    marital_mapping = {'Married': 0, 'Single': 1, 'Divorced': 2}
    card_mapping = {'Blue': 0, 'Silver': 1, 'Gold': 2, 'Platinum': 3}

    gender_encoded = gender_mapping[gender]
    income_encoded = income_mapping[income_category]
    # Add encoding for education level if needed
    # Add encoding for marital status if needed
    # Add encoding for card category if needed

    # Create input data array
    input_data = [[customer_age, gender_encoded, dependent_count, income_encoded, months_on_book, total_relationship_count,
                   months_inactive_12_mon, contacts_count_12_mon, credit_limit, total_revolving_bal, avg_open_to_buy,
                   total_amt_chng_q4_q1, total_trans_amt, total_trans_ct, total_ct_chng_q4_q1, avg_utilization_ratio,
                   education_level_college, education_level_graduate, education_level_high_school, education_level_other,
                   education_level_uneducated, divorced, married, single, card_category_blue, card_category_gold,
                   card_category_platinum, card_category_silver]]

    # Prediction button
    if st.button('Predict'):
        # Perform prediction
        prediction = predict_churn(input_data)

        # Display prediction result with styled title
        if prediction == 1:
            result_text = '<span style="color: red; font-size: 24px;">Customer is likely to churn.</span>'
        else:
            result_text = '<span style="color: green; font-size: 24px;">Customer is not likely to churn.</span>'

        st.markdown(result_text, unsafe_allow_html=True)

if __name__ == '__main__':
    main()
