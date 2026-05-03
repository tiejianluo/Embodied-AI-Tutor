# 🧠 Embodied AI Rubik's Cube Tutor

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red?logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-blue?logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

An interactive web application that transforms Rubik's Cube manipulation into learnable algebraic group structure through embodied AI tutoring. This project implements the educational framework from the paper **"An Embodied AI Tutor that Turns Rubik’s Cube Interaction into Learnable Group Structure"**, demonstrating how abstract mathematical concepts can emerge from concrete physical interaction.

**Public repository:** [https://github.com/tiejianluo/Embodied-AI-Tutor](https://github.com/tiejianluo/Embodied-AI-Tutor)

**Public app:** deploy from this repository on Streamlit Community Cloud with `app.py` as the entry file.

---

## 🎯 Overview

| Aspect | Details |
|--------|---------|
| **Language** | Python 3.8+ |
| **UI Framework** | Streamlit |
| **Visualization** | Plotly & Matplotlib |
| **Data Processing** | NumPy & Pandas |
| **Main File** | `app.py` |
| **Research Based** | Luo et al. (2026) *Nature Science of Learning* |

> [!NOTE]
> This tutor provides an interactive learning environment that translates Rubik's Cube operations into algebraic group theory concepts through reversible micro-experiments.

---

## ✨ Features

- ✅ **3D Cube Visualization** — Interactive 3D rendering of Rubik's Cube with Plotly
- ✅ **Action-to-Operator Mapping** — Translate face turns into algebraic operators
- ✅ **Reversible Micro-Experiments** — Pause, step, rewind, and replay cube operations
- ✅ **Identity and Inverse Demonstrations** — Visualize reversible operations and their properties
- ✅ **Composition and Non-Commutativity** — Explore order-dependent operation results
- ✅ **Reusable Composites (Macro-Operators)** — Identify and reuse meaningful move sequences
- ✅ **Fixed Activity Cases** — 4 carefully designed cases covering key group theory concepts
- ✅ **Predictive Assessment** — Generate questions to test understanding of group theory concepts
- ✅ **Responsive Dashboard** — Clean, intuitive UI with real-time cube manipulation
- ✅ **Mathematical Notation** — Proper LaTeX formatting for algebraic expressions
- ✅ **Case-Specific Prompts** — Targeted questions and observations for each activity case

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tiejianluo/Embodied-AI-Tutor.git
   cd Embodied-AI-Tutor
   ```

2. **Create and activate a virtual environment:**

   ```bash
   # Windows
   python -m venv .venv
   .venv\Scripts\activate

   # macOS / Linux
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app:**

   ```bash
   streamlit run app.py
   ```

5. **Open in browser:**
   Streamlit will print a URL (typically `http://localhost:8501`). Open it in your browser.

---

## 🏗️ Learning Pipeline

```
Micro-Experiment → Prediction → Observation → Explanation → Concept Reinforcement
        │               │             │              │                    │
    Cube Operation   Learner Guess   Result Display  Student Explanation  Group Theory Concept
        │               │             │              │                    │
   Reversible       Immediate       Visual         Formative          Operationalized
   Execution        Feedback        Comparison      Assessment         Mathematical Ideas
```

---

## 🎯 Activity Case: From Commutators to Conjugates

**Goal:** Verify non-commutativity and explore cycle decomposition.

**Setup:** Start from a solved state ($e$).

### 1. **Proving Non-Commutativity**
Perform $R F'$ followed by $F' R$.

$$R F' \neq F' R$$

*Prompt:* Identify the pieces that moved differently. Why does order matter?

### 2. **The Commutator $C$**
Execute the sequence $C = R F' R' F$ ("Out, Out, In, In").

*Observation:* Notice that most of the cube remains fixed, but specific corners and edges are swapped.

### 3. **Order of an Element**
Repeat the sequence $C$ six times: $C^6$.

$$(R F' R' F)^6 = e$$

*Prompt:* Why did it take 6 cycles to return to identity? (Hint: Look at the 3-cycle of edges and 2-cycle of corners).

### 4. **Conjugation (Setup Moves)**
Apply a setup move $U$, perform the commutator $C$, then undo the setup $U'$.

$$g = U (R F' R' F) U'$$

*Result:* The permutation effect of $C$ is transported to a new location on the Upper face.

---

## 🧠 Tutor Functionality

### 1. 🎮 **Activity Case Implementation**
- **Proving Non-Commutativity**: Demonstrate that $R F' \neq F' R$ through interactive comparison
- **The Commutator $C$**: Execute $C = R F' R' F$ and observe its localized effect
- **Order of an Element**: Show that $C^6 = e$ through repeated execution
- **Conjugation**: Demonstrate $g = U C U'$ to transport commutator effects

### 2. 🔄 **Interactive Cube Visualization**
- 3D rendering of Rubik's Cube with Plotly
- Step-by-step state transitions for each operation
- Real-time cube manipulation with control buttons

### 3. ⚡ **Predictive Assessment**
- Case-specific prediction questions about operation outcomes
- Multiple-choice format with immediate feedback
- Targeted prompts to reinforce conceptual understanding

### 4. 📐 **Mathematical Notation**
- Proper LaTeX formatting for algebraic expressions
- Clear presentation of group theory concepts
- Connection between physical operations and abstract algebra

---

## 📊 Evaluation Metrics

### **Conceptual Understanding** ↑
- **Definition**: Ability to map cube operations to algebraic concepts
- **Measurement**: Predictive accuracy on operation outcomes
- **Ideal**: High prediction success rate across concept types

### **Procedural Fluency** ↑
- **Definition**: Ability to execute and reverse operation sequences
- **Measurement**: Speed and accuracy of cube manipulation
- **Ideal**: Smooth execution with minimal errors

### **Transfer Performance** ↑
- **Definition**: Application of learned concepts to new contexts
- **Measurement**: Success on novel operation sequences
- **Ideal**: Strong performance on unfamiliar problems

### **Cognitive Load Reduction** ↓
- **Definition**: Manageability of information processing demands
- **Measurement**: Time spent and errors made during complex operations
- **Ideal**: Efficient problem-solving with low error rates

---

## 🎓 Learning Workflow

### Step 1: Case Selection
1. Choose an activity case from the four options:
   - Proving Non-Commutativity
   - The Commutator C
   - Order of an Element
   - Conjugation

### Step 2: Predictive Exploration
1. Observe the initial cube state (always starts solved)
2. Study the operation sequence for the selected case
3. Predict the outcome based on the provided question

### Step 3: Interactive Manipulation
1. Use control buttons to manipulate the cube
   - Step Forward/Backward through sequences
   - Rewind/Fast Forward to specific states
   - Visualize each step of the operation sequence

### Step 4: Formative Assessment
1. Answer prediction questions about operation outcomes
2. Receive immediate feedback on responses
3. Identify and correct misconceptions through targeted prompts

### Step 5: Concept Reinforcement
1. Review operation effects and algebraic properties
2. Explore the mathematical concepts behind each case
3. Connect physical cube operations to abstract group theory

---

## 📁 Code Structure

```
app.py
├── Cube Core
│   ├── Cube class with rotation logic
│   ├── Quaternion-based 3D rotation
│   ├── Color and face mapping
│   └── Operation sequence handling
│
├── Learning Framework
│   ├── Activity case implementation
│   ├── Concept-based case selection
│   ├── Predictive question engine
│   └── Case-specific prompt generation
│
├── Visualization Functions
│   ├── 3D cube rendering with Plotly
│   ├── Interactive cube manipulation
│   ├── Operation sequence visualization
│   └── Step-by-step state transitions
│
├── UI Components
│   ├── Activity case buttons (4 main cases)
│   ├── Main cube visualization area
│   ├── Operation control buttons (Step/Replay)
│   └── Assessment question interface
│
└── Streamlit App
    ├── Session state management
    ├── Custom CSS styling
    ├── Real-time cube state updates
    └── Formative assessment interface
```

---

## 🔧 Configuration & Tuning

### Learning Parameters

| Parameter | Value | Effect |
|-----------|-------|--------|
| **Activity Cases** | 4 fixed cases | Learning objective focus |
| **Sequence Length** | Case-specific | Number of operations in sequence |
| **Initial Cube State** | Solved | All cases start from solved configuration |
| **Visualization** | Interactive 3D | Cube manipulation and state transitions |

### Performance Optimization

> [!TIP]
> For optimal performance:
> - Use modern browser (Chrome/Firefox recommended)
> - Ensure sufficient GPU memory for 3D visualization
> - Close other browser tabs to reduce resource usage
> - For best experience, use a screen resolution of 1080p or higher

---

## 📚 Academic Context

This tutor implements the framework from:

**Luo, T., et al. (2026).** *An Embodied AI Tutor that Turns Rubik’s Cube Interaction into Learnable Group Structure. Nature Science of Learning.*

### Key Research Contributions:
1. **Embodied Learning Design**: Transforms concrete cube operations into abstract algebraic concepts
2. **Distributed Inquiry Cycle**: Creates a teacher-student-agent triad for collaborative learning
3. **Reversible Micro-Experiments**: Enables exploration through pause, step, rewind, and replay
4. **Cognitive Load Management**: Makes comparisons visible and repeatable to reduce learning barriers
5. **Symbolic Readouts**: Exposes operational tests for group properties (identity, inverses, commutativity)

### Abstract
How do abstract algebraic ideas emerge from concrete action, and what role can educational agents play in that process? We introduce an **embodied AI Rubik’s Cube tutor** that reframes group theory learning as an inquiry cycle distributed across a teacher–student–agent triad. Rather than presenting definitions first, the agent orchestrates short, reversible micro-experiments on a physical cube—pause, step, rewind, replay, and slow-motion—that invite learners to predict outcomes, test hypotheses, and explain contrasts. This design targets core cognitive hurdles of early group reasoning (objectifying operations, definition checking, and translating between embodied and symbolic representations), while managing cognitive load by making comparisons visible and repeatable.

Technically, the tutor learns from action–consequence data. From tuples $(o_t,a_t,o_{t+1})$, it trains a compact transition model and exposes **symbolic readouts**—operational tests for identity/inverses, composition equivalence, and commuting vs. non-commuting move pairs. These readouts drive formative prompts and misconception-focused contrasts, positioning the agent as an experiment generator and classroom assistant rather than a black-box solver.

---

## 🚀 Deployment

### Local Deployment
Follow the [Quick Start](#quick-start) instructions above.

### Streamlit Cloud Deployment
1. Push code to `https://github.com/tiejianluo/Embodied-AI-Tutor`
2. Connect repository to [Streamlit Cloud](https://streamlit.io/cloud)
3. Select branch `main`
4. Set `app.py` as main file
5. Deploy with default settings

### Docker Deployment (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🔮 Future Extensions

### Planned Features
- [ ] **Physical Cube Integration** — Connect to real Rubik's Cube hardware
- [ ] **Personalized Learning Paths** — Adaptive difficulty based on performance
- [ ] **Multi-language Support** — Extend to additional languages
- [ ] **Export Functionality** — Save learning progress and experiment results
- [ ] **Collaborative Learning** — Multi-user learning sessions

### Research Extensions
- [ ] **Generalization to Other Groups** — Apply framework to other algebraic structures
- [ ] **Long-term Learning Studies** — Track knowledge retention over time
- [ ] **Cross-cultural Evaluation** — Test with diverse learner populations
- [ ] **Teacher Dashboard** — Monitor and guide student progress

---

## 🤝 Contributing

We welcome contributions to enhance this educational tool:

1. **Report Issues**: Use GitHub Issues to report bugs or suggest features
2. **Submit Pull Requests**: Implement improvements or new features
3. **Share Use Cases**: How are you using this tutor in teaching or research?

### Development Guidelines
- Follow PEP 8 coding standards
- Include docstrings for all functions
- Add tests for new functionality
- Update documentation accordingly

---

## 📦 Dependencies

```
streamlit>=1.28.0
numpy>=1.24.0
plotly>=5.17.0
matplotlib>=3.7.0
pillow>=9.0.0
```

See `requirements.txt` for exact version specifications.

---

## Audit and Test Gates

This repository now includes claim-aware tests for the Nature SoL roadmap.

```bash
python testcode/run_all_tests.py
```

The command runs:

- legacy cube and activity checks;
- unit tests for notation parsing, condition flags, explanation scoring, transfer scoring, and export metadata;
- system tests for a Condition C learning flow;
- acceptance tests for C1-C8 paper-claim traceability.

GitHub Actions runs the same command on push and pull request. Pull requests
should fill in `.github/pull_request_template.md` with the milestone, related
claims, unit/system/acceptance evidence, and any deferred risks.

---

## 📄 License

This project is licensed under the **MIT License**.

```
Copyright (c) 2026 The Authors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

---

## 📞 Contact & Citation

For questions about the research:
- **Corresponding Author**: Tiejian Luo (tjluo@ucas.ac.cn)

If you use this tutor in your research or teaching, please cite:

```bibtex
@article{luo2026embodied,
  title={An Embodied AI Tutor that Turns Rubik's Cube Interaction into Learnable Group Structure},
  author={Luo, Tiejian and others},
  journal={Nature Science of Learning},
  year={2026},
  publisher={Nature Research}
}
```

---

*This tutor is an educational tool for exploring algebraic concepts through embodied interaction. While based on peer-reviewed research, it uses simplified representations for educational purposes.*
