import streamlit as st
from fpdf import FPDF
from datetime import date

# Configuración de la página
st.set_page_config(page_title="Cloud Inspection Assessment", layout="wide")

st.title("Formulario de Evaluación de Cloud Inspection")
st.subheader("Partner de Cisco: Typhoon Technology")
st.write("Complete este cuestionario para descubrir la arquitectura de Security recomendada para sus proyectos.")

# --- SECCIÓN 1: Información General del Proyecto ---
st.header("1. Información General del Proyecto")
col1, col2 = st.columns(2)

with col1:
    empresa = st.text_input("Nombre de la empresa")
    contacto = st.text_input("Contacto principal")
    correo = st.text_input("Correo electrónico")
    puesto = st.text_input("Puesto")

with col2:
    am_cisco = st.text_input("AM de Cisco")
    resp_best = st.text_input("Responsable de Best")
    fecha = st.date_input("Fecha de evaluación", date.today())
    vertical = st.selectbox("Vertical de negocio", 
                            ["Finanzas", "Salud", "Retail", "Manufactura", "Educación", "Gobierno", "Servicios", "Otro"])

# --- SECCIÓN 2: Dominios de Evaluación ---
st.header("2. Dominios de Evaluación de Seguridad")
st.write("Expanda cada sección para evaluar los controles en la nube.")

respuestas = {}
notas = {}

# Dominio A: Cloud Provider Controls (Pag 4)
with st.expander("A. Controles del Proveedor de Nube (Cloud Provider Controls)"):
    st.write("Evalúe la postura del CSP (Cloud Service Provider).")
    respuestas['provider_infra'] = st.selectbox(
        "Seguridad Física e Infraestructura: ¿Cómo evalúa los centros de datos y la virtualización del CSP?", 
        ["Seleccione", "Desconocida/No evaluada", "Controles ambientales básicos", "Controles estrictos con IPS y seguridad de virtualización"]
    )
    respuestas['provider_comp'] = st.selectbox(
        "Cumplimiento y Certificaciones: ¿El CSP se adhiere a estándares de la industria?", 
        ["Seleccione", "No se han validado", "Cumplimiento legal básico", "Certificaciones completas (ISO 27001, SOC 2, etc.)"]
    )
    respuestas['provider_dr'] = st.selectbox(
        "Continuidad y Respuesta a Incidentes: ¿Cuál es la capacidad del proveedor ante desastres?", 
        ["Seleccione", "Sin planes compartidos", "Notificaciones estándar de incidentes", "Mecanismos probados de failover y procedimientos claros de notificación"]
    )
    notas['provider_notas'] = st.text_area("Notas / Observaciones (Cloud Provider)", 
                                           placeholder="Ej. El cliente utiliza AWS en la región US-East. Cuentan con el reporte SOC 2 Tipo II, pero no tienen claro el SLA de respuesta a incidentes de seguridad...")

# Dominio B: Customer Controls (Pag 5-8)
with st.expander("B. Controles del Cliente (Customer Controls)"):
    st.write("Gestión administrada por el cliente: accesos, endpoints, aplicaciones y postura.")
    respuestas['cust_iam'] = st.selectbox(
        "IAM, Cifrado y Activos: ¿Cómo gestionan identidades, accesos privilegiados y cifrado de datos?", 
        ["Seleccione", "Políticas de contraseñas básicas sin cifrado fuerte", "Uso de grupos/ACLs y cifrado en tránsito", "Integración de IAM, gestión de cuentas privilegiadas y cifrado en tránsito/reposo"]
    )
    respuestas['cust_network'] = st.selectbox(
        "Seguridad de Red y Postura Cloud: ¿Cómo aseguran sus VPCs, arquitectura y cargas de trabajo?", 
        ["Seleccione", "Firewalls básicos, arquitectura no definida", "Herramientas nativas del CSP aisladas", "Uso de Cloud Security Posture Management (CSPM) y Cloud Workload Protection (CWPP)"]
    )
    respuestas['cust_monitoring'] = st.selectbox(
        "Monitoreo, Endpoints y Respuesta: ¿Cómo detectan amenazas y protegen sus dispositivos/aplicaciones?", 
        ["Seleccione", "Revisión manual de logs, AV tradicional", "Logs habilitados pero sin SIEM, análisis básico de vulnerabilidades", "Integración con SIEM/XDR, análisis continuo y protección avanzada de endpoints"]
    )
    respuestas['cust_compliance'] = st.selectbox(
        "Cumplimiento, DLP y Terceros: ¿Tienen estrategias de prevención de pérdida de datos y gestión de riesgos de terceros?", 
        ["Seleccione", "No hay políticas de DLP ni evaluación de terceros", "Cumplimiento normativo parcial (GDPR, HIPAA)", "DLP robusto, evaluación de SLAs con terceros y concientización a usuarios"]
    )
    notas['cust_notas'] = st.text_area("Notas / Observaciones (Customer Controls)", 
                                       placeholder="Ej. Tienen un Active Directory local que planean integrar con Azure AD. Falta visibilidad en los contenedores (Kubernetes) y no cuentan con una herramienta de prevención de pérdida de datos (DLP)...")

# Dominio C: Shared Controls (Pag 9)
with st.expander("C. Controles Compartidos (Shared Controls)"):
    st.write("Alineación de responsabilidades entre el cliente y el CSP.")
    respuestas['shared_resp'] = st.selectbox(
        "Responsabilidades de Políticas y Operativas: ¿Están documentadas las responsabilidades operativas (ej. implementación Zero Trust)?", 
        ["Seleccione", "No hay documentación clara", "Alineación parcial en operaciones", "Responsabilidades y políticas Zero Trust claramente documentadas"]
    )
    respuestas['shared_vuln'] = st.selectbox(
        "Vulnerabilidades Compartidas y Cumplimiento: ¿Cómo manejan la evaluación de componentes compartidos?", 
        ["Seleccione", "No se evalúan", "Revisiones esporádicas", "Evaluación continua de vulnerabilidades tecnológicas compartidas y alineación de cumplimiento"]
    )
    notas['shared_notas'] = st.text_area("Notas / Observaciones (Shared Controls)", 
                                         placeholder="Ej. Existe confusión sobre quién es responsable de parchar el sistema operativo de las instancias IaaS. Se requiere definir una matriz RACI...")

# --- SECCIÓN 3: Información Estratégica ---
st.header("3. Información Estratégica")
st.write("Calificación de la oportunidad comercial.")

col_bant1, col_bant2 = st.columns(2)
with col_bant1:
    bant_reto = st.selectbox("¿Cuál es el reto principal?", 
                             ["Seleccione", "Fin de soporte / Obsolescencia", "Brecha de seguridad reciente", "Migración a la nube", "Cumplimiento normativo", "Consolidación de vendors"])
    bant_presupuesto = st.selectbox("Presupuesto", 
                                    ["Seleccione", "Sí, presupuesto aprobado", "En proceso de aprobación", "Sin presupuesto asignado aún"])
with col_bant2:
    bant_tiempo = st.selectbox("Tiempo de implementación", 
                               ["Seleccione", "0 a 3 meses", "3 a 6 meses", "6 a 12 meses", "Más de 12 meses"])
    bant_comp = st.selectbox("Plataformas evaluadas (Competencia)", 
                             ["Seleccione", "Palo Alto / Fortinet", "Microsoft / AWS nativo", "Crowdstrike / SentinelOne", "Ninguna / Solo Cisco", "Otras"])

bant_notas = st.text_area("Detalles adicionales de la estrategia", 
                          placeholder="Ej. El cliente busca reemplazar sus firewalls perimetrales en Q3 y tienen urgencia por cumplir con la norma ISO 27001...")

# --- LÓGICA DE RECOMENDACIÓN DE PRODUCTOS ---
def generar_recomendaciones(respuestas):
    recomendaciones = []
    
    # IAM y Access
    if "básicas" in respuestas['cust_iam'] or "ACLs" in respuestas['cust_iam']:
        recomendaciones.append("- **Cisco Duo & Secure Access:** Para implementar MFA, verificar la postura de los dispositivos y asegurar el acceso bajo un enfoque Zero Trust.")
        
    # Cloud Workloads y Network
    if "básicos" in respuestas['cust_network'] or "aisladas" in respuestas['cust_network'] or "No se evalúan" in respuestas['shared_vuln']:
        recomendaciones.append("- **Cisco Cloud Application Security (Panoptica):** Para integrar la seguridad en el ciclo CI/CD (DevSecOps), asegurar APIs y brindar protección de cargas de trabajo (CWPP).")
        recomendaciones.append("- **Cisco Multicloud Defense / Secure Firewall:** Para segmentación avanzada, prevención de intrusiones y control de red multicloud.")

    # Monitoring y Endpoints
    if "manual" in respuestas['cust_monitoring'] or "sin SIEM" in respuestas['cust_monitoring']:
        recomendaciones.append("- **Cisco XDR & Secure Cloud Analytics:** Para unificar la detección de amenazas, digitalizar el entorno de la nube y automatizar la respuesta a incidentes.")
        recomendaciones.append("- **Cisco Secure Endpoint:** Para brindar protección avanzada contra malware y visibilidad de endpoints a nivel de línea de comandos.")

    # Compliance, Data and Provider
    if "No hay" in respuestas['cust_compliance'] or "Desconocida" in respuestas['provider_infra']:
        recomendaciones.append("- **Cisco Cloudlock (CASB) / Umbrella SIG:** Para asegurar el acceso a internet, prevenir la pérdida de datos sensibles (DLP) y auditar el ecosistema de aplicaciones en la nube (Shadow IT).")
        
    if not recomendaciones:
        recomendaciones.append("- **Cisco Enterprise Agreement 3.0 (Security):** Su postura de seguridad es robusta. Recomendamos un EA para consolidar licenciamiento, simplificar la gestión y escalar de forma predecible.")
        
    return recomendaciones

# --- GENERACIÓN DE PDF CORREGIDA ---
def crear_pdf(empresa, contacto, correo, puesto, am_cisco, resp_best, fecha, vertical, bant_reto, bant_presupuesto, bant_tiempo, bant_comp, bant_notas, respuestas, notas, recomendaciones):
    pdf = FPDF()
    pdf.add_page()
    
    def clean_txt(texto):
        if not texto:
            return "N/A"
        return str(texto).encode('latin-1', 'replace').decode('latin-1')
    
    try:
        pdf.image('logo_typhoon.jpg', 10, 8, 40)
        pdf.image('logo_cisco.jpg', 160, 8, 30)
    except:
        pass 
    
    pdf.ln(25)
    
    pdf.set_font("Arial", 'B', 16)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(0, 10, clean_txt("Acta de Evaluación - Cloud Inspection & Security"), ln=True, align='C')
    pdf.set_font("Arial", 'I', 11)
    pdf.cell(0, 6, clean_txt("Elaborado por: Best - Typhoon Technology"), ln=True, align='C')
    pdf.ln(10)
    
    # 1. Info General
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, clean_txt("1. Información General del Cliente"), ln=True)
    pdf.set_font("Arial", '', 10)
    
    pdf.cell(30, 6, "Empresa:", border=0)
    pdf.cell(65, 6, clean_txt(empresa), border=0)
    pdf.cell(30, 6, "Vertical:", border=0)
    pdf.cell(65, 6, clean_txt(vertical), border=0, ln=True)
    
    pdf.cell(30, 6, "Contacto:", border=0)
    pdf.cell(65, 6, clean_txt(contacto), border=0)
    pdf.cell(30, 6, "Fecha:", border=0)
    pdf.cell(65, 6, clean_txt(fecha), border=0, ln=True)
    
    pdf.cell(30, 6, "Correo:", border=0)
    pdf.cell(65, 6, clean_txt(correo), border=0)
    pdf.cell(30, 6, "AM Cisco:", border=0)
    pdf.cell(65, 6, clean_txt(am_cisco), border=0, ln=True)
    
    pdf.cell(30, 6, "Puesto:", border=0)
    pdf.cell(65, 6, clean_txt(puesto), border=0)
    pdf.cell(30, 6, "Resp. Best:", border=0)
    pdf.cell(65, 6, clean_txt(resp_best), border=0, ln=True)
    pdf.ln(5)
    
    # 2. Cuestionario (Movido antes de la info BANT)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, clean_txt("2. Respuestas de Dominios de Seguridad"), ln=True)
    
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 6, clean_txt("A. Cloud Provider Controls"), ln=True)
    pdf.set_font("Arial", '', 9)
    pdf.set_x(10) 
    pdf.multi_cell(0, 5, clean_txt(f"- Infraestructura CSP: {respuestas['provider_infra']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Cumplimiento CSP: {respuestas['provider_comp']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Continuidad y Respuesta: {respuestas['provider_dr']}"))
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(80, 80, 80)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Notas: {notas['provider_notas']}"))
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)

    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 6, clean_txt("B. Customer Controls"), ln=True)
    pdf.set_font("Arial", '', 9)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- IAM y Cifrado: {respuestas['cust_iam']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Seguridad Red y Postura: {respuestas['cust_network']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Monitoreo y Endpoints: {respuestas['cust_monitoring']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Cumplimiento y DLP: {respuestas['cust_compliance']}"))
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(80, 80, 80)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Notas: {notas['cust_notas']}"))
    pdf.set_text_color(0, 0, 0)
    pdf.ln(3)

    pdf.set_font("Arial", 'B', 10)
    pdf.cell(0, 6, clean_txt("C. Shared Controls"), ln=True)
    pdf.set_font("Arial", '', 9)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Políticas y Operaciones: {respuestas['shared_resp']}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"- Vulnerabilidades y Cumplimiento: {respuestas['shared_vuln']}"))
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(80, 80, 80)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Notas: {notas['shared_notas']}"))
    pdf.set_text_color(0, 0, 0)
    pdf.ln(5)

    # 3. BANT (Movido hasta el final)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 8, clean_txt("3. Información Estratégica (BANT)"), ln=True)
    pdf.set_font("Arial", '', 10)
    pdf.set_x(10)
    pdf.multi_cell(0, 6, clean_txt(f"Reto Principal: {bant_reto} | Presupuesto: {bant_presupuesto}"))
    pdf.set_x(10)
    pdf.multi_cell(0, 6, clean_txt(f"Tiempo: {bant_tiempo} | Competencia: {bant_comp}"))
    pdf.set_font("Arial", 'I', 9)
    pdf.set_text_color(50, 50, 50)
    pdf.set_x(10)
    pdf.multi_cell(0, 5, clean_txt(f"Detalles Adicionales: {bant_notas}"))
    pdf.ln(5)
    
    # 4. Recomendaciones
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 8, clean_txt("4. Soluciones Cisco Security Recomendadas"), ln=True)
    pdf.set_font("Arial", '', 10)
    for rec in recomendaciones:
        texto_limpio = rec.replace("**", "")
        pdf.set_x(10)
        pdf.multi_cell(0, 5, clean_txt(texto_limpio))
        pdf.ln(2)
        
    pdf.set_text_color(0, 102, 204)
    pdf.set_x(10)
    pdf.cell(0, 6, "Referencia del portafolio Cisco: https://www.cisco.com/site/us/en/products/index.html", ln=True)
    
    # Disclaimer
    pdf.ln(8)
    pdf.set_font("Arial", 'I', 8)
    pdf.set_text_color(100, 100, 100)
    disclaimer = "Nota importante: Esta información es una sugerencia preliminar generada a partir de los datos proporcionados. Queda estrictamente sujeta a los comentarios, validación técnica y diseño formal por parte de un profesional preventa o arquitecto de soluciones certificado de Typhoon Technology."
    pdf.set_x(10)
    pdf.multi_cell(0, 4, clean_txt(disclaimer))
    
    # SOLUCIÓN AL ERROR DE EXPORTACIÓN
    # Convertimos la salida de pdf.output() directamente a bytes
    return bytes(pdf.output())

# --- BOTÓN DE GENERACIÓN ---
st.divider()

def checar_completado(dict_respuestas, list_bant):
    for val in dict_respuestas.values():
        if "Seleccione" in val: return False
    for val in list_bant:
        if "Seleccione" in val: return False
    return True

if st.button("Generar Evaluación y Preparar PDF"):
    lista_bant = [bant_reto, bant_presupuesto, bant_tiempo, bant_comp]
    
    if not empresa:
        st.warning("Por favor, introduzca al menos el nombre de la empresa en la Información General.")
    elif not checar_completado(respuestas, lista_bant):
        st.warning("Asegúrese de responder todas las preguntas desplegables (Información Estratégica y Dominios) antes de generar el reporte.")
    else:
        recomendaciones = generar_recomendaciones(respuestas)
        
        st.success("¡Análisis completado exitosamente!")
        st.subheader("Sugerencia de Soluciones (Vista Previa):")
        for r in recomendaciones:
            st.markdown(r)
            
        pdf_bytes = crear_pdf(empresa, contacto, correo, puesto, am_cisco, resp_best, fecha, vertical, 
                              bant_reto, bant_presupuesto, bant_tiempo, bant_comp, bant_notas, 
                              respuestas, notas, recomendaciones)
                              
        nombre_archivo = f"Security_Assessment_CloudInspection_{empresa.replace(' ', '_')}.pdf"
        
        st.download_button(
            label="📄 Descargar PDF de la Evaluación",
            data=pdf_bytes,
            file_name=nombre_archivo,
            mime="application/pdf"
        )