FROM public.ecr.aws/d3j8x8q7/olympus-base:latest

WORKDIR /app
COPY . .

# The repo's .dockerignore drops *.jq, *.yaml and *_test.go from the build
# context; restore every tracked file so the tree is exactly the pinned commit.
RUN git reset --hard b7ebffbfc038677520df0bae4c8c2d877f88ffea && git clean -fd

RUN go mod download

RUN GOBIN=/usr/local/bin go install github.com/jstemmer/go-junit-report/v2@v2.1.0

ENV GOTOOLCHAIN=auto
ENV GOFLAGS="-mod=readonly"
ENV CGO_ENABLED=0

RUN go build ./...

CMD ["/bin/bash"]
