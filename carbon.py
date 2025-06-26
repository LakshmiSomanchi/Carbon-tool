import streamlit as st
import pandas as pd # Import pandas for handling Excel/CSV files - kept for now, but not strictly used for direct file upload in this version

# --- Configuration ---
# Set page configuration for better aesthetics and responsiveness
st.set_page_config(
    page_title="GreenImpact: Carbon & ESG Tool",
    page_icon="🌿",
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
    
    All calculations are adjusted to be on a monthly basis for consistency with output.
    """
    electricity_emission = electricity_kwh * 0.8
    car_emission = car_km * 0.2
    
    # FIX: Convert annual flights_hours to monthly by dividing by 12
    # The slider collects annual hours, but the output is monthly.
    monthly_flights_hours = flights_hours / 12
    flights_emission = monthly_flights_hours * 90 
    
    waste_emission = waste_kg * 0.5
    
    # New calculations for advanced features
    meat_emission = (meat_servings_week * 4) * 5 # Convert weekly to monthly (approx 4 weeks/month), then by factor
    clothing_emission = clothing_items_month * 10
    streaming_emission = (streaming_hours_day * 30) * 0.05 # Convert daily to monthly (approx 30 days/month), then by factor

    total_emission = (electricity_emission + car_emission + flights_emission + 
                      waste_emission + meat_emission + clothing_emission + streaming_emission)
    return total_emission

# --- Streamlit App Layout ---

# Header Section
st.title("🌿 GreenImpact: NGO Carbon, ESG, and Social Impact Tool")
st.markdown("---")
st.markdown(
    """
    Welcome to GreenImpact! This tool is designed to support NGOs in understanding,
    measuring, and advocating for environmental and social sustainability.
    Explore carbon footprint estimation, ESG principles, carbon markets, and relevant
    regulations.
    """
)
st.markdown("---")

# Carbon Footprint Calculator Section (Now nested in an expander)
st.header("👣 Individual/Small Organization Carbon Footprint Estimator")
st.markdown(
    """
    While our primary focus is broader NGO support, understanding individual or
    small organizational carbon footprints can be a valuable educational and
    awareness-raising tool.
    """
)
with st.expander("Estimate Your Carbon Footprint"):
    st.markdown(
        """
        Please enter your estimated monthly consumption or activity data below
        to get an estimated carbon footprint.
        """
    )
    electricity_kwh = st.slider(
        "Monthly Electricity Usage (kWh)", 
        0, 1000, 150, 5, 
        key="electricity_kwh_slider", # Added key
        help="Estimate your monthly electricity consumption in kilowatt-hours (kWh)."
    )
    car_km = st.slider(
        "Monthly Car Travel (km)", 
        0, 2000, 300, 10, 
        key="car_km_slider", # Added key
        help="Approximate distance you travel by car each month."
    )
    flights_hours = st.slider(
        "Annual Flight Hours (total for all flights)", 
        0, 100, 5, 1, 
        key="flights_hours_slider", # Added key
        help="Total hours spent flying in a year. This will be converted to a monthly average for calculation."
    )
    waste_kg = st.slider(
        "Monthly Waste Generated (kg)", 
        0, 100, 10, 1, 
        key="waste_kg_slider", # Added key
        help="Estimated weight of non-recyclable waste you generate monthly."
    )
    
    st.markdown("---")
    st.subheader("Advanced Consumption Data (Optional)")
    
    meat_servings_week = st.slider(
        "Weekly Meat Servings (red meat)",
        0, 20, 4, 1,
        key="meat_servings_slider", # Added key
        help="Approximate number of red meat servings per week. Higher numbers indicate higher footprint."
    )
    clothing_items_month = st.slider(
        "Monthly New Clothing Items Purchased",
        0, 10, 1, 1,
        key="clothing_items_slider", # Added key
        help="Number of new clothing items you typically purchase in a month."
    )
    streaming_hours_day = st.slider(
        "Daily Video Streaming Hours",
        0, 8, 2, 0.5,
        key="streaming_hours_slider", # Added key
        help="Hours spent streaming video content daily (e.g., Netflix, YouTube). Data centers consume energy!"
    )


    if st.button("Calculate My Footprint", key="calculate_personal_footprint"):
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
        if flights_hours / 12 * 90 > 50: # Check the *monthly* impact of flights for recommendations
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

# New Section: Carbon Markets, Pricing & Credits
st.header("💲 Carbon Markets, Pricing & Credit Opportunities for NGOs")
st.markdown(
    """
    Understanding carbon markets is crucial for NGOs involved in environmental
    conservation and sustainable development.
    """
)

with st.expander("Carbon Pricing Mechanisms"):
    st.subheader("Carbon Tax")
    st.write(
        """
        A **carbon tax** directly prices carbon emissions, making polluting activities
        more expensive. Governments set a price per tonne of carbon dioxide (or CO2e) emitted.
        * **Implication for NGOs:** Can advocate for the implementation or increase of carbon taxes
          to incentivize greener practices and generate revenue for climate initiatives.
        """
    )
    st.subheader("Cap-and-Trade Systems (Emissions Trading Schemes - ETS)")
    st.write(
        """
        **Cap-and-trade systems** set a limit (cap) on total emissions allowed, and then issue
        allowances (permits to emit) up to that cap. Companies can buy and sell these allowances
        (trade), creating a market price for carbon.
        * **Implication for NGOs:** Can monitor the effectiveness of ETS, advocate for stricter
          caps, and help develop projects that generate carbon credits under such systems.
        """
    )

with st.expander("Sectors/Activities Eligible for Carbon Credits"):
    st.subheader("What are Carbon Credits?")
    st.write(
        """
        A **carbon credit** (or offset credit) is a measurable, verifiable, and permanent
        reduction of one metric tonne of carbon dioxide equivalent (CO2e) emissions.
        They are generated by projects that reduce, remove, or avoid GHG emissions.
        """
    )
    st.subheader("Common Project Types for Carbon Credits:")
    st.write(
        """
        * **Renewable Energy Projects:** Solar, wind, hydro power replacing fossil fuel-based electricity.
        * **Energy Efficiency Projects:** Improving industrial processes, commercial/residential buildings.
        * **Waste Management:** Capturing methane from landfills, composting, waste-to-energy.
        * **Forestry and Land Use (Nature-Based Solutions):** Reforestation, afforestation, avoided deforestation (REDD+),
          sustainable land management, blue carbon initiatives (mangroves, seagrass).
        * **Agriculture:** Improved agricultural practices that sequester carbon or reduce N2O/CH4 emissions.
        * **Industrial Process Improvements:** Reducing emissions from chemical production, cement, etc.
        * **Carbon Capture, Utilization, and Storage (CCUS):** Emerging technologies to capture CO2 from industrial sources or atmosphere.
        """
    )
    st.subheader("Role of NGOs in Carbon Credit Projects:")
    st.write(
        """
        NGOs often play a critical role in developing, verifying, and implementing carbon credit projects,
        especially those related to community-based initiatives, forestry, and sustainable agriculture.
        They can also help communities and organizations access finance through carbon markets.
        """
    )

st.markdown("---")

# ESG Awareness Section (retained)
st.header("🌎 Understanding ESG (Environmental, Social, Governance)")
st.markdown(
    """
    ESG factors are critical for assessing the sustainability and ethical impact of organizations.
    For an NGO, understanding these connections is crucial for advocacy, partnerships, and impact.
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
        * **Connection for NGOs:** Advocating for environmental protection, promoting sustainable resource use,
          and working on climate resilience projects directly addresses the 'E' pillar.
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
        * **Connection for NGOs:** Directly aligns with NGOs focused on human rights, community development,
          social justice, and fair labor practices. Advocating for corporate social responsibility.
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
        * **Connection for NGOs:** Promoting transparency, ethical leadership, and accountability
          in corporations and government, which underpins effective environmental and social initiatives.
        """
        )

st.markdown("---")

# New Section: ESG Laws and Regulations in India
st.header("⚖️ ESG Regulatory Landscape in India")
st.markdown(
    """
    For NGOs operating in India, understanding the evolving regulatory framework for ESG is essential
    for compliance, advocacy, and identifying opportunities for impact.
    *(This section provides a high-level overview. Always refer to official government sources for specifics.)*
    """
)

with st.expander("Key Indian ESG-Related Laws & Initiatives"):
    st.subheader("Business Responsibility and Sustainability Reporting (BRSR)")
    st.write(
        """
        * **Mandated by SEBI (Securities and Exchange Board of India):** Replaced the Business Responsibility Report (BRR).
        * **Purpose:** Requires the top 1000 listed companies (by market capitalization) to disclose their ESG performance
          against specific parameters and principles.
        * **Relevance for NGOs:** NGOs can leverage BRSR data for corporate engagement, research, and advocacy
          to encourage greater sustainability and accountability.
        """
    )
    st.subheader("Companies (CSR Policy) Rules, 2014 (and amendments)")
    st.write(
        """
        * **Mandatory CSR:** Requires companies meeting certain profit/turnover/net worth criteria to spend 2% of their
          average net profits of the preceding three years on Corporate Social Responsibility (CSR) activities.
        * **Relevance for NGOs:** This is a direct funding mechanism and partnership opportunity for NGOs, as companies
          often partner with NGOs to implement their CSR initiatives in areas like education, health, and environmental protection.
        """
    )
    st.subheader("Environmental Protection Act, 1986 & Rules")
    st.write(
        """
        * **Broad Framework:** A comprehensive law for the protection and improvement of the environment.
          It provides for the regulation of environmental pollution, hazardous substances, and environmental clearances.
        * **Relevance for NGOs:** Used by environmental NGOs for litigation, advocacy against pollution,
          and promoting adherence to environmental standards.
        """
    )
    st.subheader("Water (Prevention and Control of Pollution) Act, 1974 & Air (Prevention and Control of Pollution) Act, 1981")
    st.write(
        """
        * **Sector-Specific:** These acts deal with the prevention, control, and abatement of water and air pollution,
          respectively, establishing pollution control boards.
        * **Relevance for NGOs:** Crucial for NGOs working on water quality, air quality, and public health issues,
          enabling them to engage with regulatory bodies and industry.
        """
    )
    st.subheader("National Green Tribunal Act, 2010")
    st.write(
        """
        * **Specialized Tribunal:** Established a specialized judicial body for effective and expeditious disposal of
          cases relating to environmental protection and conservation of forests and other natural resources.
        * **Relevance for NGOs:** Provides a fast-track legal recourse for environmental grievances and violations,
          often utilized by environmental NGOs.
        """
    )
    st.subheader("India's Climate Commitments (NDCs, Net-Zero Target)")
    st.write(
        """
        * **International Agreements:** India's Nationally Determined Contributions (NDCs) under the Paris Agreement
          and its commitment to achieve Net-Zero emissions by 2070.
        * **Relevance for NGOs:** NGOs play a vital role in monitoring progress, advocating for more ambitious targets,
          and implementing ground-level projects that contribute to climate goals.
        """
    )

st.markdown("---")

# Simulated Live News and Updates Section (retained and re-emphasized)
st.header("📰 ESG News & Updates (Simulated)")
st.markdown(
    """
    Stay informed about the latest developments and trends in global and Indian ESG and sustainability.
    For NGOs, keeping track of these updates is vital for strategic planning, identifying funding
    opportunities, and informing advocacy efforts.
    *(In a full application, this section would fetch live, relevant news from dedicated APIs
    or curated sources, focusing on NGO-specific insights where possible.)*
    """
)
with st.expander("Recent Headlines (Simulated)"):
    st.write("- **June 2025:** Major Indian corporations announce enhanced sustainability targets aligned with BRSR frameworks.")
    st.write("- **May 2025:** New government initiatives launched to boost renewable energy adoption in rural India.")
    st.write("- **April 2025:** Discussions at the NGT highlight increasing legal actions against industrial pollution in key regions.")
    st.write("- **March 2025:** NGOs collaborate on a nationwide campaign for sustainable water management in drought-prone areas.")
    st.write("- **February 2025:** International funds show increased interest in ESG-compliant projects within India's social sector.")
    
st.markdown("---")

# GHG Protocol Tools (No longer includes Excel upload option)
st.header("📊 GHG Protocol Tool (Placeholder)")
st.markdown(
    """
    This section provides placeholders for GHG Protocol-based calculation tools.
    *(Note: These are placeholders. In a full implementation, the logic from these GHG Protocol
    Excel tools would be translated into Python code and integrated directly into this app,
    allowing for specific calculations relevant to organizational emissions.)*
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
        emissions from manufacturing processes). This is critical for an NGO managing its own facilities or fleet.
        
        *Example inputs: Fuel type, quantity consumed, vehicle type, refrigerant leaks.*
        """
    )
    st.info("Coming soon: Interactive calculator for Scope 1 emissions!")
elif ghg_tool_selection == "GHG Protocol Tool 2: Scope 2 Emissions (Indirect from Electricity)":
    st.markdown(
        """
        **GHG Protocol Tool 2: Scope 2 Emissions (Indirect from Electricity)**
        This section would focus on indirect emissions from the generation of purchased electricity,
        steam, heating, and cooling consumed by your organization. Essential for an NGO to track its energy consumption impact.
        
        *Example inputs: Purchased electricity (kWh), location (grid emission factor for your region/country).*
        """
    )
    st.info("Coming soon: Interactive calculator for Scope 2 emissions!")
elif ghg_tool_selection == "GHG Protocol Tool 3: Scope 3 Emissions (Value Chain) - Categories (e.g., Business Travel)":
    st.markdown(
        """
        **GHG Protocol Tool 3: Scope 3 Emissions (Value Chain) - Categories**
        This tool would cover various categories of indirect emissions that occur in the value chain
        of the reporting company/NGO, both upstream and downstream. This could include:
        * **Business travel:** Flights, train, car travel for staff.
        * **Employee commuting:** Staff travel to and from work.
        * **Waste generated in operations:** Waste sent to landfills, incineration.
        * **Purchased goods and services:** Emissions embedded in items/services your NGO buys.
        * **Investments:** For NGOs with endowments or significant investments.
        
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
    consider consulting with environmental specialists and legal experts for specific ESG compliance.
    """
)
st.markdown("---")

st.caption("Developed with ❤️ for Carbon, ESG & Social Impact")
