# Smart Fit Recommendations

This project is a recommendation system designed to provide personalized clothing recommendations. It uses modern machine learning techniques to analyze user preferences and item features, delivering relevant and timely suggestions.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

-   Python 3.11
-   Poetry for dependency management

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/smart-fit-recs.git
    cd smart-fit-recs
    ```

2.  **Install dependencies:**

    This project uses `uv` and a `Makefile` to streamline the setup process. To install the required packages and set up the environment, run:

    ```bash
    make install
    ```

## Configuration

1.  **Create a `.env` file:**

    The project requires API keys and other configuration to be stored in a `.env` file in the project root. You can create one by copying the example file:

    ```bash
    cp .env.example .env
    ```

2.  **Add your credentials:**

    Open the `.env` file and add your API keys:

    ```
    HOPSWORKS_API_KEY="your_hopsworks_api_key"
    OPENAI_API_KEY="your_openai_api_key"
    ```

## Usage

The core logic of this project is explored and demonstrated in the Jupyter notebooks located in the `notebooks/` directory.

To run the feature engineering notebook, you can use the following `make` command:

```bash
make feature-engineering
```

Alternatively, you can launch Jupyter and run the notebooks manually:

1.  **Activate the virtual environment:**

    ```bash
    source .venv/bin/activate
    ```

2.  **Launch Jupyter:**

    ```bash
    jupyter notebook
    ```

3.  **Open a notebook:**

    Navigate to the `notebooks/` directory in the Jupyter interface and open one of the notebooks (e.g., `computing_features.ipynb`) to get started.
