# List commands
default:
    @"{{ just_executable() }}" --list

# Run the tests
test *args:
    opensafely exec python:latest pytest {{ args }}
