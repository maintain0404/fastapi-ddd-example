# Initialize.

## Summary
This repository is based on 4-Layered Architecture. Mapping of the architecture and this repository is shown below.

### Mapping with 4 layered Architecture
- `4 layered Architecture` -> `This repository directories`  
- `Infra` -> `provider`  
- `persistence` -> `domain/repo`, `trait/repo`, `usecase`.  
- `Application` -> `domain`, `trait`, `usecase`.  
- `Presentation` -> `handler`, `core`  

## Background
- None

## Subject
- Build initial architecture as DDD style.

## Detail
### provider
This component has responsibility to support implementing core business logic. It has similar role of infra layer in 4-layered architecture. For example, controlling infra, wrapping external library, custom data structure and so on are included here.

### domain/trait
Domain and trait are separated into their respective subdomains of interest and are solely responsible for them. Difference of domain and trait is if they are concrete or not. Domain is concrete, but trait is not. Trait is implementation of special features of domain and can be used as parent class or mixin class of domain classes.

### Use Case
Use case unite domains. This merges various domains and builds final business logic.

### handler
Handler has responsibility on how our business logic result is shown to client. FastAPI framework is used here.

### util
Util directory has responsibility on code readability and ease of implementation.

### core
This builds initial components of FastAPI application.

## Alternatives
- None

## ETC
- None