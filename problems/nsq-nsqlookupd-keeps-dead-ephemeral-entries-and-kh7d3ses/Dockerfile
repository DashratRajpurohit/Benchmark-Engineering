FROM public.ecr.aws/d3j8x8q7/olympus-base:latest

WORKDIR /app

COPY go.mod go.sum ./

RUN go mod download && \
    go install github.com/jstemmer/go-junit-report/v2@v2.1.0

COPY . .

RUN go build ./...

CMD ["/bin/bash"]
