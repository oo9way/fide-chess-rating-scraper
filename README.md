
# Scraper ranking table FIDE.COM

Get ranking table in once!



## Installation

Clone the project

```bash
  git clone https://github.com/muhammadusufs/fide-chess-rating-scraper
```

Go to the project directory

```bash
  cd fide-chess-rating-scraper
```
Run terminal command
```bash
  pip install -r requirements.txt

```
    
## Usage/Examples
Scraping data
```python
# Categories : open, women, juniors, girls
# Data type : list, file

data = ParseFideRating(category, data_type)

```
Getting result
```python
print(data.get_data()) # Prints all data 
```
