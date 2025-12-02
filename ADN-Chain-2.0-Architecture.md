# ADN-Chain 2.0 – Identity, Recovery & Ledger Architecture

## Visión

ADN-Chain 2.0 propone una identidad digital soberana con:

- Identidad sin dependencia de seed phrases expuestas.
- Recuperación autónoma basada en señales reales, sin guardianes humanos.
- Verificabilidad global del historial personal mediante anclaje criptográfico.
- SDKs y APIs pensados para integraciones Web2/Web3.

## Arquitectura de alto nivel

- **Nodo ADN-Chain (dispositivo)**
  - Core Service
  - Crypto & Identity (BIP-39/BIP-32, Ed25519, etc.)
  - Ledger Engine (LPV)
  - Recovery Engine (ADN-R²)
  - IA-Lite (motor de riesgo local)
  - Secure Comms Stack (Noise_XX + QUIC/WebRTC)
  - Anchor Client
  - UI Adapter

- **Backend no-custodial**
  - Anchor Service: recibe raíces Merkle y simula publicación en L1
  - Verification Gateway: verifica pruebas de anclaje

- **Red L1**
  - Capa externa para anclaje de Merkle roots (Celestia/Avail u otras)

Los diagramas C4 (System, Container, Component) residen en `/diagrams`.

## Componentes clave

- **Ledger personal verificable (LPV)**: hashchain, Merkle y snapshots para auditabilidad compacta.
- **Recuperación autónoma ADN-R²**: integridad de dispositivo, multidispositivo y liveness.
- **IA-Lite de riesgo**: inferencia local, no decisional.
- **Comunicación segura**: Noise_XX sobre QUIC/WebRTC con formatos IPLD/CBOR.
- **Anclajes periódicos**: publicación de raíces Merkle en una L1 económica.
- **Interoperabilidad**: compatibilidad con UCAN e IPLD.

## Estructura del repositorio (monorepo)

```text
/README.md
/LICENSE
/.gitignore
/WORKSPACE
/BUILD.bazel

/src
  /core           # Lógica central del nodo (Rust/Go)
  /crypto         # BIP-39, BIP-32, firmas
  /ledger         # LPV: hashchain + Merkle + snapshots
  /recovery       # ADN-R²: integridad + multidispositivo + liveness
  /ai-lite        # Motor de riesgo local (Python)
  /comms          # Noise_XX + transporte seguro
  /anchors        # Cliente de anclaje
  /ui-adapter     # Modelos de datos para UI/web
  /utils          # Utilidades compartidas

/backend
  /anchor-service           # Microservicio TS
  /verification-gateway     # Microservicio TS
  /config                   # Configuración YAML/JSON

/web
  /app                      # Frontend (React/Next.js)
  /sdk
    /ts-sdk                 # SDK TypeScript
    /py-sdk                 # SDK Python
    /go-sdk                 # SDK Go
  /cli
    /rust-cli               # CLI en Rust

/api
  /openapi.yaml             # Especificación OpenAPI 3.0.3

/diagrams
  /c4-system.svg
  /c4-container.svg
  /c4-component.svg
  /sequence-adnr2.svg
  /sequence-anchor.svg

/docs
  /RFC-ADN-Chain-0001.md
  /architecture.md
  /threat-model.md
  /data-model.md
  /api-reference.md
  /readme-core.md
  /readme-backend.md
  /readme-web.md

/paper
  /ADN-Chain-IEEEtran.tex
  /ADN-Chain-Zenodo-Paper.pdf
  /ADN-Chain-Metadata.json

/jira
  /ADN-Chain-Backlog.csv

/devops
  /docker
  /k8s
  /terraform
  /ci
```

## Tecnologías clave

- Rust/Go para núcleo del nodo.
- TS/Node.js para microservicios de anclaje y verificación.
- React/Next.js para frontend.
- SDKs en TypeScript, Python y Go.
- Noise_XX + QUIC/WebRTC para transporte seguro.
- IPLD/CBOR como formatos interoperables.
- Anclaje en L1 económica (Celestia/Avail u otras).

## Cómo empezar (visión de alto nivel)

1. Desplegar el nodo ADN-Chain en el dispositivo (core + LPV + ADN-R²).
2. Configurar la pila de comunicaciones segura (Noise_XX sobre QUIC/WebRTC).
3. Arrancar Anchor Service y Verification Gateway en backend no-custodial.
4. Sincronizar snapshots del LPV y programar anclajes periódicos de raíces Merkle.
5. Integrar aplicaciones cliente mediante los SDKs (Web2/Web3) y UI adapters.

## Roadmap resumido

- v0.2.0: expansión multidominio del LPV y mejoras del motor de riesgo local.
- v1.0.0: consolidación científica del dataset y automatización completa con Zenodo.
- Validaciones extendidas por dominio y preparación para versiones shard.

## Licencia

MIT para componentes propios; las fuentes externas mantienen sus licencias originales.
