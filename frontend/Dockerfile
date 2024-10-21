# -- stg -- #

FROM node:22.9.0-bullseye AS stg

WORKDIR /app

COPY package.json .
COPY yarn.lock .
COPY .yarnrc.yml .

RUN corepack enable yarn && corepack prepare yarn@4
RUN corepack yarn install --immutable

COPY . .

# -- dev -- #

FROM stg AS dev

WORKDIR /app

ENV NODE_ENV=development
ENV HOST=0.0.0.0
EXPOSE 3000

CMD [ "corepack", "yarn", "dev" ]

# -- build for deploy -- #

FROM node:22.9.0-bullseye-slim AS build

WORKDIR /app

COPY --from=stg /app .

RUN corepack enable yarn && corepack prepare yarn@4
RUN corepack yarn workspaces focus --production

ENV NODE_ENV=production
ENV HOST=0.0.0.0
ENV PORT=443

RUN corepack yarn build

# -- deploy -- #

FROM gcr.io/distroless/nodejs22-debian12 AS deploy

COPY --from=build /app/.output/ /.output/

EXPOSE 3000/tcp
CMD ["/.output/server/index.mjs"]


