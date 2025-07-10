## Contributing to LLM Cognitive Crawler

Thank you for your interest in contributing to the LLM Cognitive Crawler project! This project aims to advance our understanding of AI cognition through systematic Bayesian inverse planning.

### 🎯 How to Contribute

#### For Researchers
- **Cognitive Science Experts**: Help validate hypothesis frameworks and experimental designs
- **AI Safety Researchers**: Contribute to bias detection and safety assessment methods
- **Statisticians**: Review Bayesian methodologies and validation approaches
- **Ethicists**: Provide guidance on moral reasoning scenarios and bias detection

#### For Developers
- **Python Developers**: Implement core architecture and analysis tools
- **ML Engineers**: Optimize model interfaces and data processing pipelines
- **Frontend Developers**: Build visualization dashboards and user interfaces
- **DevOps Engineers**: Enhance infrastructure and deployment systems

### 📋 Types of Contributions

#### Research Contributions
- **Scenario Development**: Create new cognitive probing scenarios
- **Hypothesis Refinement**: Improve cognitive pattern hypotheses
- **Validation Studies**: Design and conduct validation experiments
- **Literature Review**: Contribute to theoretical foundations

#### Technical Contributions
- **Core Features**: Implement new analysis capabilities
- **Bug Fixes**: Identify and resolve issues
- **Performance**: Optimize processing and analysis speed
- **Documentation**: Improve guides, tutorials, and API docs

#### Quality Assurance
- **Testing**: Write comprehensive test suites
- **Code Review**: Participate in peer review process
- **Validation**: Verify research reproducibility
- **Security**: Identify and address security concerns

### 🚀 Getting Started

#### 1. Set Up Development Environment
```bash
# Fork and clone the repository
git clone https://github.com/your-username/llm-cognitive-crawler.git
cd llm-cognitive-crawler

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt
pip install -e .

# Set up pre-commit hooks
pre-commit install
```

#### 2. Configure API Access
```bash
# Copy environment template
cp config/api_keys.example.env config/api_keys.env

# Edit with your API keys (never commit this file!)
# - OpenAI API key
# - Anthropic API key
# - Other model provider keys
```

#### 3. Run Tests
```bash
# Run full test suite
pytest

# Run with coverage
pytest --cov=llm_cognitive_crawler

# Run specific test category
pytest tests/test_scenarios.py
```

### 📚 Development Guidelines

#### Code Quality Standards
- **Python Style**: Follow PEP 8, enforced by Black
- **Type Hints**: Use comprehensive type annotations
- **Docstrings**: Google-style docstrings for all public functions
- **Testing**: Maintain >90% test coverage
- **Security**: No hardcoded secrets or sensitive data

#### Research Standards
- **Reproducibility**: All experiments must be reproducible
- **Documentation**: Comprehensive methodology documentation
- **Validation**: Statistical validation for all claims
- **Ethics**: IRB approval for human subjects research

#### Git Workflow
```bash
# Create feature branch
git checkout -b feature/cognitive-hypothesis-framework

# Make changes and commit with descriptive messages
git commit -m "Add utilitarian reasoning hypothesis with validation tests"

# Push and create pull request
git push origin feature/cognitive-hypothesis-framework
```

### 🔍 Code Review Process

#### Pull Request Requirements
- [ ] **Description**: Clear description of changes and motivation
- [ ] **Testing**: All tests pass, new tests for new features
- [ ] **Documentation**: Updated docs for API changes
- [ ] **Research**: Methodology documentation for research changes
- [ ] **Security**: No exposed secrets or vulnerabilities

#### Review Criteria
- **Correctness**: Code works as intended
- **Quality**: Follows style and architecture guidelines
- **Testing**: Adequate test coverage and quality
- **Documentation**: Clear and comprehensive
- **Research Validity**: Sound experimental design and analysis

### 🧪 Research Contribution Guidelines

#### Experimental Design
- **Hypothesis**: Clear, testable hypotheses
- **Methods**: Rigorous experimental design
- **Controls**: Appropriate control conditions
- **Statistics**: Proper statistical analysis
- **Validation**: Cross-validation and replication

#### Data and Analysis
- **Reproducibility**: All analysis code available
- **Documentation**: Clear methodology documentation
- **Validation**: Independent validation when possible
- **Ethics**: Ethical guidelines compliance

#### Publication Standards
- **Open Science**: Open data and code when possible
- **Transparency**: Full methodology disclosure
- **Replication**: Support for independent replication
- **Community**: Engage with research community

### 🚨 Reporting Issues

#### Bug Reports
- **Title**: Clear, descriptive title
- **Environment**: Python version, OS, dependencies
- **Steps**: Minimal reproduction steps
- **Expected**: Expected behavior
- **Actual**: Actual behavior with error messages

#### Feature Requests
- **Use Case**: Clear description of need
- **Proposed Solution**: Detailed feature description
- **Research Value**: Research or practical benefits
- **Implementation**: Suggested implementation approach

#### Research Questions
- **Background**: Theoretical or empirical motivation
- **Question**: Specific, answerable research question
- **Methodology**: Proposed research approach
- **Impact**: Expected research or practical impact

### 🤝 Community Guidelines

#### Respectful Collaboration
- **Inclusive**: Welcome all backgrounds and perspectives
- **Constructive**: Provide helpful, constructive feedback
- **Professional**: Maintain professional communication
- **Ethical**: Uphold highest ethical standards

#### Knowledge Sharing
- **Open**: Share knowledge and expertise freely
- **Patient**: Help newcomers learn and contribute
- **Collaborative**: Work together toward common goals
- **Transparent**: Open about methods and limitations

### 🏆 Recognition

Contributors will be recognized through:
- **Code Contributors**: Listed in AUTHORS.md
- **Research Contributors**: Co-authorship on relevant publications
- **Major Contributors**: Special recognition in project documentation
- **Community Contributors**: Acknowledgment in presentations and papers

### 📞 Getting Help

- **Technical Questions**: Create GitHub issue with "question" label
- **Research Questions**: Start GitHub Discussion
- **Private Matters**: Email project maintainers
- **Real-time Chat**: Join project Discord/Slack (if available)

### 📄 Legal

By contributing, you agree that:
- Your contributions will be licensed under the MIT License
- You have the right to contribute the content
- Your contributions are your own original work or properly attributed

---

**Ready to contribute?** Check out our [good first issues](https://github.com/prof-schacht/llm-cognitive-crawler/labels/good%20first%20issue) or reach out to discuss how you can help advance AI cognitive research!
