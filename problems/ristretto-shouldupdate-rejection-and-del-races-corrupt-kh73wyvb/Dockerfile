FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest

WORKDIR /app

# Copy dependency files and install pinned test tooling
COPY go.mod go.sum ./

RUN go mod download && \
    go install github.com/jstemmer/go-junit-report/v2@v2.1.0

# Copy project source
COPY . .

# Verify the project builds
RUN go build ./...

CMD ["/bin/bash"]
