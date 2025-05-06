# Calcake – Calculadora de Ingredientes por Tamaño 🧁

**Calcake** es una aplicación sencilla desarrollada en Python con **PyQt5** que permite calcular la cantidad de ingredientes necesarios para preparar una receta según el tamaño deseado. Es ideal para pastelería, repostería o cualquier proceso escalable.

---

## 📋 Características

- Interfaz gráfica moderna con PyQt5.
- Fórmula base: `Base = (1/3) * Tamaño - 1`
- Cada ingrediente se calcula como múltiplo de esa base:
  - Huevos: ×1
  - Harina: ×25
  - Azúcar: ×5
  - Cacao: ×30
- Compatible con Windows, macOS y Linux.
- Opción de exportar como `.exe` usando PyInstaller.

---

## 🧰 Requisitos

- Python 3.8 o superior
- PyQt5
- PyInstaller (opcional, para crear el ejecutable)

---

## 🚀 Instalación

### 1. Clona este repositorio:

```bash
git clone https://github.com/jpgotopo/calcake.git
cd calcake
