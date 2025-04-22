import streamlit as st

st.title("Calculadora de Gases - Ley Combinada de Boyle y Mariotte")
st.markdown("**Fórmula general:** (P₁V₁) / (n₁T₁) = (P₂V₂) / (n₂T₂)")
st.markdown("**Unidades:** atm, L, K, mol")

# Opción a calcular
opcion = st.selectbox(
    "¿Qué variable deseas calcular?",
    ["Presión final (P₂)", "Volumen final (V₂)", "Temperatura final (T₂)", "Moles finales (n₂)"]
)

# Ingreso de variables iniciales y finales (menos la variable a calcular)
if opcion == "Presión final (P₂)":
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    V2 = st.number_input("Volumen final V₂ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.01)
    n1 = st.number_input("Moles iniciales n₁ (mol)", min_value=0.01)
    n2 = st.number_input("Moles finales n₂ (mol)", min_value=0.01)
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    
    if st.button("Calcular P₂"):
        P2 = (P1 * V1 * n2 * T2) / (V2 * n1 * T1)
        st.success(f"Presión final P₂ = {P2:.3f} atm")

elif opcion == "Volumen final (V₂)":
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    P2 = st.number_input("Presión final P₂ (atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.01)
    n1 = st.number_input("Moles iniciales n₁ (mol)", min_value=0.01)
    n2 = st.number_input("Moles finales n₂ (mol)", min_value=0.01)

    if st.button("Calcular V₂"):
        V2 = (P1 * V1 * n2 * T2) / (P2 * n1 * T1)
        st.success(f"Volumen final V₂ = {V2:.3f} L")

elif opcion == "Temperatura final (T₂)":
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    P2 = st.number_input("Presión final P₂ (atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    V2 = st.number_input("Volumen final V₂ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    n1 = st.number_input("Moles iniciales n₁ (mol)", min_value=0.01)
    n2 = st.number_input("Moles finales n₂ (mol)", min_value=0.01)

    if st.button("Calcular T₂"):
        T2 = (P2 * V2 * n1 * T1) / (P1 * V1 * n2)
        st.success(f"Temperatura final T₂ = {T2:.3f} K")

elif opcion == "Moles finales (n₂)":
    P1 = st.number_input("Presión inicial P₁ (atm)", min_value=0.01)
    P2 = st.number_input("Presión final P₂ (atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial V₁ (L)", min_value=0.01)
    V2 = st.number_input("Volumen final V₂ (L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial T₁ (K)", min_value=0.01)
    T2 = st.number_input("Temperatura final T₂ (K)", min_value=0.01)
    n1 = st.number_input("Moles iniciales n₁ (mol)", min_value=0.01)

    if st.button("Calcular n₂"):
        n2 = (P1 * V1 * T2 * n1) / (P2 * V2 * T1)
        st.success(f"Moles finales n₂ = {n2:.3f} mol")
