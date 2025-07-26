import matplotlib.ticker as mtick
import matplotlib.pyplot as plt  
import streamlit as st
import pandas as pd
import numpy as np

# to run program, terminal > streamlit run main.py

def main():

    st.title('Portfolio Growth Simulator')
    with st.expander('CSV Format Instructions'):
        st.markdown("""
            Upload a CSV with these columns:
            - `Ticker`: stock symbol (e.g. TSLA)
            - `Shares`: how many shares
            - `Current Price`: price per share (can include $) """)
        uploaded_file = st.file_uploader('Upload your portfolio CSV',type=["csv"])
        if uploaded_file:
            df = user_portfolio(uploaded_file)
            st.subheader('📊 Cleaned Portfolio') # st.subheader lets me display a subheader 
            st.dataframe(df) # shows df as an interactive table in your app.
            tickers = df['Ticker'].unique().tolist()

            view_option = st.selectbox('Select view',['Total Portfolio'] + tickers)
            weekly_investment = st.number_input('weekly investment ($)', min_value=0, value=900) # lets user enter number they can not be below 0 the default is 900
            years = st.slider('years to simulate',1 ,50, 20) # I made a slider from 1 to 50 the default is 20    
            annual_growth = st.slider('Expected Annual Growth (%)',0, 30, 8) # slider for Annual Growth from 0% to 30% default is 8
            volatility = st.slider('Volatility Level',0.0, 0.2, 0.05)
            if st.button('Run Simulation'):
                    projections = future_value(df, years, weekly_investment, annual_growth,volatility, view_option)
                    if view_option == 'Total Portfolio':
                        plot_projection(projections) # the simulates future growth 
                    
                    elif view_option in tickers:
                        plot_single_stock(view_option, projections)



def user_portfolio(uploaded_file):

    try:
        df = pd.read_csv(uploaded_file) # reads a CSV file and turns it into a DataFrame

        for col in df.columns:
            if (df[col].dtype) == 'object':
                df[col] = df[col].str.replace('\t', '', regex=False)

        df['Current Price'] = df['Current Price'].replace({r'\$': '', ',': ''}, regex=True).astype(float) # cleaned 'Current Pice' by removing $ and , also converted to float
        df = df.dropna(subset=['Current Price'])  # drop rows where price couldn't be converted

        return df
    
    except Exception as e:
        st.error("Error processing CSV")
        return None



def future_value(df,years,weekly_investment,annual_growth,volatility,selected_ticker=None): # Simulate future growth
    
    total_weeks = years * 52  # I converted years to weeks
    weekly_multiplier = (1+annual_growth/100) ** (1/total_weeks) # Convert annual growth rate (%) to a weekly compounding multiplier
    total_value = [0] * total_weeks
    
    if selected_ticker and selected_ticker != "Total Portfolio":
        df = df[df['Ticker'] == selected_ticker] #only include rows where the Ticker column matches the selected_ticker
        weekly_contribution_per_row = weekly_investment

    else:
        weekly_contribution_per_row = weekly_investment / len(df)

    # I will loop through each row in the portfolio DataFrame
    for _,row in df.iterrows(): # _ ignores the index number
        
        current_price = row['Current Price']
        shares = float(row['Shares'])
        value = current_price * shares

        individual_value = []
    
        for week in range(total_weeks):
            random_factor = 1.0 if volatility == 0.0 else np.random.normal(loc=1.0, scale=volatility)
            value *= weekly_multiplier * random_factor
            value = max(value, 0)
            value += weekly_contribution_per_row
            individual_value.append(value)
        
        total_value = [total_value[i] + individual_value[i] for i in range(total_weeks)]

   
    return total_value



def plot_single_stock(tickers, values):
    
    fig, ax = plt.subplots() # I made a figure and axis using matplotlib
    ax.plot(values, label= tickers)
    ax.set_title(f'Projected Growth: {tickers}') # main title
    ax.set_xlabel('years') # Weeks appears below the axis

    ax.set_xticks([i * 52 for i in range(0, len(values) // 52 + 1, max(1, len(values) // (52 * 10)))])
    ax.set_xticklabels([str(i) for i in range(0, len(values) // 52 + 1, max(1, len(values) // (52 * 10)))])
    
    ax.set_ylabel('Portfolio Value') # Portfolio Value appears  on the Y axis
    ax.legend(loc='upper left') # adds a box to show which line belongs to what stock
    
    final_value = values[-1]
    st.markdown(f"### Projected Value for {tickers}: `${final_value:,.2f}`")
    
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    ax.grid(True) # turns on grid lines
    st.pyplot(fig)



def plot_projection(total_value):

    fig, ax = plt.subplots() # I made a figure and axis using matplotlib
    ax.plot(total_value, label='Total Portfolio')
    ax.set_title('Projected Portfolio Growth') # main title
    ax.set_xlabel('Years') # Weeks appears below the axis

    ax.set_xticks([i * 52 for i in range(0, len(values) // 52 + 1, max(1, len(values) // (52 * 10)))])
    ax.set_xticklabels([str(i) for i in range(0, len(values) // 52 + 1, max(1, len(values) // (52 * 10)))])

    ax.set_ylabel('Portfolio Value') # Portfolio Value appears  on the Y axis
    ax.legend(loc='upper left') # adds a box to show which line belongs to what stock
    
    final_value = total_value[-1]
    st.markdown(f"### Projected Portfolio Value: `${final_value:,.2f}`")
    
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('${x:,.0f}'))
    ax.grid(True) # turns on grid lines
    st.pyplot(fig)






if __name__ == "__main__":
    main()