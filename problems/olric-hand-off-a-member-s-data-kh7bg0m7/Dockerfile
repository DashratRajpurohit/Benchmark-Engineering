FROM public.ecr.aws/d3j8x8q7/olympus-base:latest

WORKDIR /app

# Copy dependency files and install pinned test tooling
COPY go.mod go.sum ./

RUN go mod download && \
    go install github.com/jstemmer/go-junit-report/v2@v2.1.0

# Copy project source
COPY . .

RUN go build ./... && go vet ./...

CMD ["/bin/bash"]
