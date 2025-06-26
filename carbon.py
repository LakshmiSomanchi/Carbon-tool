import streamlit as st
import pandas as pd # Import pandas for handling Excel/CSV files

# --- Configuration ---
# Set page configuration for better aesthetics and responsiveness
st.set_page_config(
    page_title="GreenImpact: Carbon & ESG Tool",
    page_icon="�",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Helper Functions (for calculations) ---
def calculate_carbon_footprint(electricity_kwh, car_km, flights_hours, waste_kg, 
                                meat_servings_week, clothing_items_month, streaming_hours_day):
    """
    Calculates an estimated carbon footprint based on user inputs.
    Conversion factors are simplified for demonstration.
    - Electricity: 0.8 kg CO2e/kWh (approx. global average for grid electricity)
    - Car: 0.2 kg CO2e/km (average petrol car)
    - Flights: 90 kg CO2e/hour (approx. for short/medium haul, simplified)
    - Waste: 0.5 kg CO2e/kg (simplified, for landfill waste)
    - Meat: 5 kg CO2e/serving (simplified for red meat)
    - Clothing: 10 kg CO2e/item (simplified for new purchases)
    - Streaming: 0.05 kg CO2e/hour (simplified, data center energy)
    """
    electricity_emission = electricity_kwh * 0.8
    car_emission = car_km * 0.2
    flights_emission = flights_hours * 90
    waste_emission = waste_kg * 0.5
    
    # New calculations for advanced features
    meat_emission = (meat_servings_week * 4) * 5 # Convert weekly to monthly, then by factor
    clothing_emission = clothing_items_month * 10
    streaming_emission = (streaming_hours_day * 30) * 0.05 # Convert daily to monthly, then by factor

    total_emission = (electricity_emission + car_emission + flights_hours + 
                      waste_emission + meat_emission + clothing_emission + streaming_emission)
    return total_emission

# --- Streamlit App Layout ---

# Header Section
st.title("🌿 GreenImpact: Carbon Footprint & ESG Tool")
st.markdown("---")
st.markdown(
    """
    Welcome to GreenImpact! This tool helps you estimate your basic carbon footprint
    and understand its connection to broader Environmental, Social, and Governance (ESG) principles.
    """
)
st.markdown("---")

# Carbon Footprint Calculator Section
st.header("👣 Your Carbon Footprint Calculator")
st.markdown(
    """
    Please enter your estimated monthly consumption or activity data below.
    This will help us calculate your estimated carbon emissions.
    """
)

# Input Fields
with st.expander("Enter Your Consumption Data"):
    electricity_kwh = st.slider(
        "Monthly Electricity Usage (kWh)", 
        0, 1000, 150, 5, 
        help="Estimate your monthly electricity consumption in kilowatt-hours (kWh)."
    )
    car_km = st.slider(
        "Monthly Car Travel (km)", 
        0, 2000, 300, 10, 
        help="Approximate distance you travel by car each month."
    )
    flights_hours = st.slider(
        "Annual Flight Hours (total for all flights)", 
        0, 100, 5, 1, 
        help="Total hours spent flying in a year. Divide by 12 for monthly average if needed."
    )
    waste_kg = st.slider(
        "Monthly Waste Generated (kg)", 
        0, 100, 10, 1, 
        help="Estimated weight of non-recyclable waste you generate monthly."
    )
    
    st.markdown("---")
    st.subheader("Advanced Consumption Data (Optional)")
    
    meat_servings_week = st.slider(
        "Weekly Meat Servings (red meat)",
        0, 20, 4, 1,
        help="Approximate number of red meat servings per week. Higher numbers indicate higher footprint."
    )
    clothing_items_month = st.slider(
        "Monthly New Clothing Items Purchased",
        0, 10, 1, 1,
        help="Number of new clothing items you typically purchase in a month."
    )
    streaming_hours_day = st.slider(
        "Daily Video Streaming Hours",
        0, 8, 2, 0.5,
        help="Hours spent streaming video content daily (e.g., Netflix, YouTube). Data centers consume energy!"
    )


if st.button("Calculate My Footprint"):
    total_co2 = calculate_carbon_footprint(
        electricity_kwh, car_km, flights_hours, waste_kg,
        meat_servings_week, clothing_items_month, streaming_hours_day
    )
    
    st.markdown("---")
    st.subheader(f"✨ Your Estimated Monthly Carbon Footprint: **{total_co2:.2f} kg CO2e**")
    st.info("*(CO2e = Carbon Dioxide Equivalent, a standard unit for measuring carbon footprints)*")
    
    st.markdown("---")
    st.header("🌱 Recommendations for Reduction")
    st.markdown(
        """
        Based on your estimated footprint, here are some general recommendations to help reduce your impact:
        """
    )
    
    # Specific recommendations based on input values (simple logic for demonstration)
    if electricity_kwh > 100:
        st.write("- **Electricity:** Consider switching to LED lights, unplugging electronics when not in use, and exploring renewable energy options for your home/office.")
    if car_km > 200:
        st.write("- **Transportation:** Opt for public transport, cycling, walking, or carpooling more often. Regular vehicle maintenance also helps!")
    if flights_hours > 0:
        st.write("- **Flights:** For unavoidable travel, consider carbon offsetting programs. Explore virtual meetings or train travel as alternatives where possible.")
    if waste_kg > 5:
        st.write("- **Waste:** Focus on the 'Reduce, Reuse, Recycle' hierarchy. Compost organic waste, buy products with minimal packaging, and avoid single-use items.")
    if meat_servings_week > 2:
        st.write("- **Diet:** Incorporate more plant-based meals into your diet. Reducing red meat consumption has a significant positive environmental impact.")
    if clothing_items_month > 1:
        st.write("- **Consumption:** Buy less, choose durable and ethically produced clothing, and explore second-hand options.")
    if streaming_hours_day > 1:
        st.write("- **Digital Footprint:** Be mindful of your digital consumption. Consider lower resolution streaming or downloading content for offline viewing when possible.")
    
    st.write("- **General:** Support local, sustainable businesses, consume less meat, and educate others about sustainable practices.")

st.markdown("---")

# ESG Awareness Section
st.header("🌎 Understanding ESG")
st.markdown(
    """
    Your carbon footprint is a direct measure of your environmental impact, but it also ties into broader
    Environmental, Social, and Governance (ESG) factors. For an NGO, understanding these connections is crucial.
    """
)

with st.expander("What is ESG?"):
    st.write(
        """
        ESG stands for **Environmental, Social, and Governance**. It's a framework used to assess
        an organization's performance beyond traditional financial metrics, focusing on its
        sustainability and ethical impact.
        """
    )
    st.markdown("---")
    st.subheader("Environmental (E)")
    st.write(
        """
        This category relates to the impact an organization has on the natural environment.
        Your carbon footprint falls directly into this 'E' pillar.
        * **Examples:** Climate change strategies, resource depletion (water, energy), pollution (air, water, land),
            biodiversity, deforestation.
        * **Connection to your footprint:** Reducing your energy consumption (electricity), choosing greener
            transport options, and managing waste directly contribute to positive environmental outcomes.
        """
    )
    st.markdown("---")
    st.subheader("Social (S)")
    st.write(
        """
        This focuses on how an organization manages relationships with its employees, suppliers,
        customers, and the communities where it operates.
        * **Examples:** Labor practices, diversity and inclusion, human rights, community engagement,
            customer privacy, health and safety.
        * **Connection to your footprint:** A large carbon footprint can contribute to air pollution,
            which disproportionately affects vulnerable communities (social justice). Conversely,
            adopting clean energy can improve community health.
        """
    )
    st.markdown("---")
    st.subheader("Governance (G)")
    st.write(
        """
        This deals with an organization's leadership, executive pay, audits, internal controls,
        and shareholder rights. It ensures ethical and responsible decision-making.
        * **Examples:** Board diversity, executive compensation, anti-corruption policies,
            transparency, lobbying, political contributions.
        * **Connection to your footprint:** Good governance ensures that environmental policies
            are implemented effectively and transparently, and that social impacts are considered
            in strategic decisions. For an NGO, strong governance builds trust and ensures mission effectiveness.
        """
        )

st.markdown("---")

# Simulated Live News and Updates Section
st.header("📰 ESG News & Updates")
st.markdown(
    """
    Stay informed about the latest developments in the world of ESG and sustainability!
    *(In a full application, this section would fetch live news from a dedicated API.)*
    """
)
with st.expander("Recent Headlines (Simulated)"):
    st.write("- **June 2025:** Major companies announce new net-zero targets for 2040, accelerating climate action.")
    st.write("- **May 2025:** New regulations proposed to increase transparency in corporate supply chains, focusing on labor rights.")
    st.write("- **April 2025:** Investment firms see a significant shift towards ESG-compliant portfolios, driven by younger investors.")
    st.write("- **March 2025:** Breakthrough in sustainable packaging materials offers promising alternative to plastics.")
    st.write("- **February 2025:** Global summit concludes with renewed commitments to biodiversity conservation.")
    
st.markdown("---")

# Excel Based Calculator / Data Integration Section
st.header("📊 Data & Tool Integration")
st.markdown(
    """
    Here, you can either upload an Excel file for general data viewing or
    select a pre-configured GHG Protocol tool for specific calculations.
    """
)

# Option to select between Excel Upload or GHG Protocol Tools
tool_option = st.radio(
    "Choose an option:",
    ("Upload Excel File", "Use GHG Protocol Tool (Placeholder)"),
    key="tool_option_selector"
)

if tool_option == "Upload Excel File":
    uploaded_file = st.file_uploader("Upload an Excel File (.xlsx)", type=["xlsx"])

    if uploaded_file is not None:
        try:
            # Read the Excel file into a pandas DataFrame
            df = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully! Here's a preview:")
            st.dataframe(df)

            st.markdown("---")
            st.subheader("Next Steps for Uploaded Data:")
            st.markdown(
                """
                * **Data Analysis:** You could perform various analyses on this data using Python's data science libraries (like pandas).
                * **Custom Calculators:** The data from your Excel file could feed into more specific, custom calculators built directly into this app.
                * **Reporting:** Generate reports or visualizations based on the uploaded data for your NGO's stakeholders.
                * **Integration:** For complex Excel formulas, consider translating them into Python code within this Streamlit app for direct execution.
                """
            )
        except Exception as e:
            st.error(f"Error reading the Excel file: {e}")
            st.info("Please ensure it's a valid .xlsx file and not corrupted.")
    else:
        st.info("Upload an Excel file to see its contents here.")

elif tool_option == "Use GHG Protocol Tool (Placeholder)":
    st.markdown("---")
    st.subheader("GHG Protocol Tools (Placeholder)")
    st.markdown(
        """
        *(Note: These are placeholders. In a full implementation, the logic from these GHG Protocol
        Excel tools would be translated into Python code and integrated directly into this app.)*
        """
    )

    ghg_tool_selection = st.selectbox(
        "Select a GHG Protocol Tool:",
        ["Select a tool...", 
         "GHG Protocol Tool 1: Scope 1 Emissions (Direct)", 
         "GHG Protocol Tool 2: Scope 2 Emissions (Indirect from Electricity)", 
         "GHG Protocol Tool 3: Scope 3 Emissions (Value Chain) - Categories (e.g., Business Travel)"],
        key="ghg_tool_selector"
    )

    if ghg_tool_selection == "GHG Protocol Tool 1: Scope 1 Emissions (Direct)":
        st.markdown(
            """
            **GHG Protocol Tool 1: Scope 1 Emissions (Direct)**
            This section would contain inputs and calculations for direct emissions from
            sources owned or controlled by your organization (e.g., fuel combustion in company vehicles,
            emissions from manufacturing processes).
            
            *Example inputs: Fuel type, quantity consumed, vehicle type.*
            """
        )
        st.info("Coming soon: Interactive calculator for Scope 1 emissions!")
    elif ghg_tool_selection == "GHG Protocol Tool 2: Scope 2 Emissions (Indirect from Electricity)":
        st.markdown(
            """
            **GHG Protocol Tool 2: Scope 2 Emissions (Indirect from Electricity)**
            This section would focus on indirect emissions from the generation of purchased electricity,
            steam, heating, and cooling consumed by your organization.
            
            *Example inputs: Purchased electricity (kWh), location (grid emission factor).*
            """
        )
        st.info("Coming soon: Interactive calculator for Scope 2 emissions!")
    elif ghg_tool_selection == "GHG Protocol Tool 3: Scope 3 Emissions (Value Chain) - Categories (e.g., Business Travel)":
        st.markdown(
            """
            **GHG Protocol Tool 3: Scope 3 Emissions (Value Chain) - Categories**
            This tool would cover various categories of indirect emissions that occur in the value chain
            of the reporting company, both upstream and downstream. This could include:
            * Business travel
            * Employee commuting
            * Waste generated in operations
            * Purchased goods and services
            
            *Example inputs for Business Travel: Travel distance, mode of transport (air, rail, car).*
            """
        )
        st.info("Coming soon: Interactive calculator for specific Scope 3 categories!")
    elif ghg_tool_selection == "Select a tool...":
        st.info("Please select a GHG Protocol tool from the dropdown above to see its description.")
        

st.markdown("---")
st.markdown(
    """
    This tool is a starting point. For more detailed analysis or organizational reporting,
    consider consulting with environmental specialists.
    """
)
st.markdown("---")

st.caption("Developed with ❤️ for Carbon, ESG & Social Impact")
