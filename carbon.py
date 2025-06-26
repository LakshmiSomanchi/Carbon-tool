import streamlit as st

# --- Configuration ---
# Set page configuration for better aesthetics and responsiveness
st.set_page_config(
    page_title="GreenImpact: Carbon & ESG Tool",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- Helper Functions (for calculations) ---
def calculate_carbon_footprint(electricity_kwh, car_km, flights_hours, waste_kg):
    """
    Calculates an estimated carbon footprint based on user inputs.
    Conversion factors are simplified for demonstration.
    - Electricity: 0.8 kg CO2e/kWh (approx. global average for grid electricity)
    - Car: 0.2 kg CO2e/km (average petrol car)
    - Flights: 90 kg CO2e/hour (approx. for short/medium haul, simplified)
    - Waste: 0.5 kg CO2e/kg (simplified, for landfill waste)
    """
    electricity_emission = electricity_kwh * 0.8
    car_emission = car_km * 0.2
    flights_emission = flights_hours * 90
    waste_emission = waste_kg * 0.5
    
    total_emission = electricity_emission + car_emission + flights_emission + waste_emission
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

if st.button("Calculate My Footprint"):
    total_co2 = calculate_carbon_footprint(
        electricity_kwh, car_km, flights_hours, waste_kg
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
st.markdown(
    """
    This tool is a starting point. For more detailed analysis or organizational reporting,
    consider consulting with environmental specialists.
    """
)
st.markdown("---")

st.caption("Developed with ❤️ for Carbon, ESG & Social Impact")
