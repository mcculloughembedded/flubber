# Command Reference

Help for any command in *main.sh* can be viewed using the *--help* switch for that command.

## Create a new component
```
flubber/scripts/main.sh new-component=<component-name>
```

## Build image
```
podman build -t unit-tests -f dockerfile .
```

## Run tests for all components
```
flubber/scripts/main.sh run
```

## Run tests for specific components
```
flubber/scripts/main.sh run --components=<comma separated list of component-names>
```

## Remove logs and output for all components
```
flubber/scripts/main.sh clean
```

## Remove logs and output specific components
```
flubber/scripts/main.sh clean --components=<comma separated list of component-names>
```
