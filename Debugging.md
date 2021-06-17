# Working with dockerised app

## Mounting source

The source folder can be mount in docker-compose for add-hoc changes view

```yaml
volumes:           
    - ./app/src:/src
```

## For debuggin with VSCode:

- expose debug port in compose:
```yaml
ports:
    - 3000:3000
```
- setup python debugger:
```python
import ptvsd
ptvsd.enable_attach(address=('0.0.0.0', 3000))
```

To add configuration:  
Run -> Add Configuration ... -> Attach Remote -> Type Host and port  
Setup local path to the soucecode and path to the source in the container:  
```json
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}/app/src",
                    "remoteRoot": "/src"
                }
            ]
```
In VSCode the debugging needs to be started with debugging configuration running  
The breakpoint should be triggered from the querry from the fronend.