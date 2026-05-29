FROM mcr.microsoft.com/devcontainers/python:3.11

# Evita prompts interactivos
ENV DEBIAN_FRONTEND=noninteractive

# Actualiza pip
RUN pip install --upgrade pip

# Instala librerías cuánticas
RUN pip install \
    qiskit \
    pennylane \
    pennylane-qiskit \
    qiskit-aer \
    jupyter \
    ipykernel

# Opcional: herramientas útiles
RUN pip install numpy scipy matplotlib pandas

# Configurar directorio de trabajo
WORKDIR /workspace