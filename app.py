import streamlit as st

R = 0.0821  # L·atm/(mol·K)

st.title("Calculadora de Gases Ideales")

ley = st.selectbox("Selecciona una ley para resolver", [
    "Ecuación Universal de los Gases Ideales",
    "Ley de Boyle y Mariotte",
    "Ley de Charles",
    "Ley de Gay-Lussac"
])

if ley == "Ecuación Universal de los Gases Ideales":
    opcion = st.radio("¿Qué variable deseas calcular?", ["Presión (P)", "Volumen (V)", "Temperatura (T)", "Número de moles (n)"])

    if opcion == "Presión (P)":
        V = st.number_input("Volumen (L)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        if st.button("Calcular Presión"):
            P = (n * R * T) / V
            st.success(f"Presión = {P:.3f} atm")

    elif opcion == "Volumen (V)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        if st.button("Calcular Volumen"):
            V = (n * R * T) / P
            st.success(f"Volumen = {V:.3f} L")

    elif opcion == "Temperatura (T)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        V = st.number_input("Volumen (L)", min_value=0.01)
        n = st.number_input("Número de moles (mol)", min_value=0.01)
        if st.button("Calcular Temperatura"):
            T = (P * V) / (n * R)
            st.success(f"Temperatura = {T:.3f} K")

    elif opcion == "Número de moles (n)":
        P = st.number_input("Presión (atm)", min_value=0.01)
        V = st.number_input("Volumen (L)", min_value=0.01)
        T = st.number_input("Temperatura (K)", min_value=0.01)
        if st.button("Calcular Número de moles"):
            n = (P * V) / (R * T)
            st.success(f"Número de moles = {n:.3f} mol")

elif ley == "Ley de Boyle y Mariotte":
    P1 = st.number_input("Presión inicial (P1, atm)", min_value=0.01)
    V1 = st.number_input("Volumen inicial (V1, L)", min_value=0.01)
    V2 = st.number_input("Volumen final (V2, L)", min_value=0.01)
    if st.button("Calcular Presión final (P2)"):
        P2 = (P1 * V1) / V2
        st.success(f"Presión final P2 = {P2:.3f} atm")

elif ley == "Ley de Charles":
    V1 = st.number_input("Volumen inicial (V1, L)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial (T1, K)", min_value=0.01)
    T2 = st.number_input("Temperatura final (T2, K)", min_value=0.01)
    if st.button("Calcular Volumen final (V2)"):
        V2 = (V1 * T2) / T1
        st.success(f"Volumen final V2 = {V2:.3f} L")

elif ley == "Ley de Gay-Lussac":
    P1 = st.number_input("Presión inicial (P1, atm)", min_value=0.01)
    T1 = st.number_input("Temperatura inicial (T1, K)", min_value=0.01)
    T2 = st.number_input("Temperatura final (T2, K)", min_value=0.01)
    if st.button("Calcular Presión final (P2)"):
        P2 = (P1 * T2) / T1
        st.success(f"Presión final P2 = {P2:.3f} atm")
