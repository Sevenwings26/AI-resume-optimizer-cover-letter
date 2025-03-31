File Structure

resume-optimizer/
│── app/
│   │── __init__.py
│   │── templates/              
│   │   │── auth/              # Login/Signup templates
│   │── static/                
│   │── web/                  
│   │   │── routes.py
│   │── api/                  
│   │   │── routes.py
│   │── auth/                  # New auth module
│   │   │── __init__.py
│   │   │── routes.py          # Auth routes (email + Google)
│   │   │── services.py        # Auth logic (register, login, OAuth)
│   │   │── models.py          # User model
│   │── extensions.py          # Flask-SQLAlchemy, Flask-Login, etc.
│── config.py                 
│── main.py                   
│── .env                      

## AI Resume Optimizer

### Description
analyzes job description and suggest resume improvement, and ask the resume should be update with the improvement.
pip install Flask 