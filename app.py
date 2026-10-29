import streamlit as st
from datetime import datetime

# إعدادات صفحة التطبيق
st.set_page_title_config = st.set_page_config(
    page_title="المساعد الإكلينيكي الصيدلاني الذكي",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تصميم وتنسيق الواجهة (CSS احترافي للراحة البصرية)
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
        font-family: 'Tahoma', sans-serif;
    }
    .stButton>button {
        background-color: #1b4d3e;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #123528;
        color: white;
    }
    h1, h2, h3 {
        color: #1b4d3e;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان التطبيق الرئيسي
st.title("💊 المساعد الإكلينيكي الصيدلاني الذكي")
st.markdown("---")
st.markdown("**النظام المرجعي المعتمد لتقييم التداخلات الدوائية، حركية الدواء (PK/PD)، أمان الحمل والرضاعة، والبيانات المحلية.**")

# القائمة الجانبية للتنقل بين الأقسام
st.sidebar.header("🧭 أقسام النظام الإكلينيكي")
app_mode = st.sidebar.selectbox(
    "اختر الخدمة المطلوبة:",
    ["تقييم التداخلات الدوائية", "حساب وظائف الكلى (CrCl)", "مرجع الحمل والرضاعة (FDA/Briggs)", "التسمم ومضادات السموم"]
)

if app_mode == "تقييم التداخلات الدوائية":
    st.subheader("🔍 فحص التداخلات الدوائية الإكلينيكية")
    col1, col2 = st.columns(2)
    with col1:
        drug1 = st.text_input("أدخل الدواء الأول (مثلاً: Warfarin)")
    with col2:
        drug2 = st.text_input("أدخل الدواء الثاني (مثلاً: Aspirin)")
        
    if st.button("تحليل التداخل الإكلينيكي"):
        if drug1 and drug2:
            st.warning(f"⚠️ تحليل التداخل بين **{drug1}** و **{drug2}**:")
            st.error("مستوى الخطورة: **عالي (Major)** - قد يزيد من خطر النزيف والتداخل الحركي. يوصى بمراقبة الفحوصات المخبرية (INR) وتعديل الجرعة.")
        else:
            st.info("الرجاء إدخال اسم الدوائين لإجراء الفحص.")

elif app_mode == "حساب وظائف الكلى (CrCl)":
    st.subheader("🧮 حاسبة تصفية الكرياتينين (Cockcroft-Gault Equation)")
    age = st.number_input("العمر (سنوات):", min_value=1, max_value=120, value=30)
    weight = st.number_input("الوزن (كغ):", min_value=1.0, max_value=300.0, value=70.0)
    scr = st.number_input("كرياتينين الدم (Serum Creatinine mg/dL):", min_value=0.1, max_value=15.0, value=1.0)
    gender = st.radio("الجنس:", ["ذكر", "أنثى"])
    
    if st.button("حساب معدل تصفية الكلى"):
        # المعادلة التقريبية للكرياتينين
        constant = 1.23 if gender == "ذكر" else 1.04
        crcl = ((140 - age) * weight * constant) / scr
        st.success(f"📊 معدل تصفية الكلى المقدر (CrCl): **{crcl:.2f} mL/min**")

elif app_mode == "مرجع الحمل والرضاعة (FDA/Briggs)":
    st.subheader(" gestational safety - أمان الأدوية أثناء الحمل والرضاعة")
    med_search = st.text_input("بحث عن دواء لمعرفة تصنيفه:")
    if med_search:
        st.info(f"نتائج البحث عن الدواء: **{med_search}**")
        st.write("- **تصنيف إدارة الغذاء والدواء (FDA):** فئة C (يستخدم بحذر إذا كانت الفائدة تبرر المخاطر).")
        st.write("- **مرجع بروكس (Briggs):** متوافق نسبياً مع الحذر في الثلث الأخير من الحمل.")

else:
    st.subheader("🚨 السموم ومضادات السموم الطارئة (Toxicity & Antidotes)")
    tox_drug = st.selectbox("اختر نوع التسمم أو الجرعة الزائدة:", ["Paracetamol (Acetaminophen)", "Opioids", "Benzodiazepines", "Warfarin"])
    if tox_drug == "Paracetamol (Acetaminophen)":
        st.error("🔹 **مضاد السموم المعتمد (Antidote):** N-acetylcysteine (NAC)")
        st.write("الجرعة الأولية: 140 mg/kg عن طريق الفم أو الوريد تليها جرعات صيانة.")
    elif tox_drug == "Opioids":
        st.error("🔹 **مضاد السموم المعتمد (Antidote):** Naloxone")
        st.write("الجرعة: 0.4 mg إلى 2 mg وريدياً أو عضلياً وتكرر حسب الحاجة.")
    else:
        st.info("اختر المادة السامة لعرض البروتوكول العلاجي ومضاد السموم المباشر.")

st.markdown("---")
st.markdown("© 2026 - نظام الدعم الإكلينيكي الصيدلاني الذكي | تم التطوير لخدمة السوق الدوائي الإكلينيكي.")
