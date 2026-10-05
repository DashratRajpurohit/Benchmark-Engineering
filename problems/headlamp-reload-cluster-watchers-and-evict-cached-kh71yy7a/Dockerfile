FROM public.ecr.aws/d3j8x8q7/olympus-base-go:latest

WORKDIR /app

# Copy module files first so the dependency download layer is cached
# independently of source changes. Versions are pinned by go.mod/go.sum.
COPY backend/go.mod backend/go.sum ./backend/
RUN cd backend && go mod download

COPY . .

# Pre-compile the backend so the container works fully offline.
RUN cd backend && go build ./...

CMD ["/bin/bash"]
