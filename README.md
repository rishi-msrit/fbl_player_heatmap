# Football Player Heatmap Generator

A **Streamlit web app** to visualize football player movements on the pitch using **StatsBomb Open Data**(Please note that the statsbomb statistics used here is a free-to-use one and so the data is limited. The app generates interactive heatmaps for selected players.

Please go easy on the website,let it load,as the data model used here is of huge chunk and generate a large cache which the streamlit finds tought to handle.
---

## **Features**

- Select **competition** and **season**.
- Choose a **team** and a **player**.
- Generate **dynamic heatmaps** showing player activity on the pitch.
- Works entirely in your browser via **Streamlit Cloud**.
- Always loads fresh data from StatsBomb.

---

## **Live Demo**

Access the live app here:https://fbl-player-heatmap.streamlit.app/

---

## **Installation (Local)**

1. Clone the repository:

```
git clone https://github.com/rishi-msrit/fbl_player_heatmap.git
cd fbl_player_heatmap
```


## Install dependencies
```
pip install -r requirements.txt
```

## Run the app locally
```
streamlit run app.py
```

## Dependencies

Python 3.x (I used 3.11)
Streamlit
StatsBombPy
mplsoccer
matplotlib
pandas
numpy
requests_cache

## Project Structure
```
player_heatmap_app/
│
├─ app.py                  # Main Streamlit app
├─ requirements.txt        # Python dependencies
└─ README.md               # Project description (this file)
 
```

## Notes
Data is sourced from StatsBomb Open Data
Streamlit Cloud handles dependencies via requirements.txt.
No caching is used to avoid storage issues, ensuring fresh data on every load.

### Auther: Rishi R
