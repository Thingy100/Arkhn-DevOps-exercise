FROM python:3
COPY . .
RUN pip install Flask==1.1.2
RUN python -m pip install requests
EXPOSE 5000
EXPOSE 5001
CMD python3 solver.py
