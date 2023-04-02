FROM node:19-alpine 

RUN npm install -g localtunnel
COPY ./Dockerfiles/scripts/node.sh node.sh

CMD ["sh", "node.sh"]