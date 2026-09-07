FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest

WORKDIR /app
COPY . .

RUN go mod download

RUN GOBIN=/usr/local/bin go install github.com/jstemmer/go-junit-report/v2@v2.1.0

ENV GOFLAGS="-mod=readonly"
ENV CGO_ENABLED=0

RUN go build ./...
RUN go vet ./cmd/zoekt-index/... ./cmd/zoekt-git-index/... ./gitindex/... ./index/...

CMD ["/bin/bash"]
