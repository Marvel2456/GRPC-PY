FROM python
WORKDIR /team_server
COPY ./team_server.py /team_server/team_server.py
# COPY ./requirement.txt /team_server/requirement.txt
RUN pip install -r requirement.txt
CMD [ "python", "team_server.py" ]