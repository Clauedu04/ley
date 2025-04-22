import streamlit as st

st.title("Calculadora de Gases - Ley Combinada de Boyle y Mariotte (moles constantes)")
st.markdown("**Fórmula usada:** (P₁V₁) / T₁ = (P₂V₂) / T₂")
st.markdown("**Unidades:** atm, L, K")

# Opción a calcular
opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ["Presión final (P₂)", "Volumen final (V₂)", "Temperatura final (T₂)"]
)

# Ingreso de variables
if opcion == "Presión final (P₂)":
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    V2 = st.number_input("Volumen final V₂ (L)", min_value=0.01)
    T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.01)

    if st.button("Calcular P₂"):
        P2 = (P1 * V1 * T2) / (V2 * T1)
        st.success(f"Presión final P₂ = {P2:.3f} atm")

elif opcion == "Volumen final (V₂)":
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    P2 = st.number_input("Presión final P₂ (atm)", min_value=0.01)
    T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.01)

    if st.button("Calcular V₂"):
        V2 = (P1 * V1 * T2) / (P2 * T1)
        st.success(f"Volumen final V₂ = {V2:.3f} L")

elif opcion == "Temperatura final (T₂)":
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    P2 = st.number_input("Presión final P₂ (atm)", min_value=0.01)
    V2 = st.number_input("Volumen final V₂ (L)", min_value=0.01)

    if st.button("Calcular T₂"):
        T2 = (P2 * V2 * T1) / (P1 * V1)
        st.success(f"Temperatura final T₂ = {T2:.3f} K")
