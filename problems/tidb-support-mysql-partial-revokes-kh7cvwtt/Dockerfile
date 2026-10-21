FROM public.ecr.aws/d3j8x8q7/olympus-base:latest

WORKDIR /app

# Copy dependency files of both modules and install pinned test tooling
COPY go.mod go.sum ./
COPY pkg/parser/go.mod pkg/parser/go.sum ./pkg/parser/

RUN go mod download && \
    go install github.com/jstemmer/go-junit-report/v2@v2.1.0

# Copy project source
COPY . .

# Verify the server builds and compile the test binaries of the packages the
# tests use, so test runs start from a warm build cache
RUN go build -o /dev/null ./cmd/tidb-server && \
    go test -tags intest -count=1 -exec /bin/true ./pkg/privilege/privileges ./pkg/executor/test/simpletest ./pkg/executor/test/showtest

CMD ["/bin/bash"]
