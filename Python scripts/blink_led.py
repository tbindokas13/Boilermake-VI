from GPIOLibrary import GPIOProcessor
import time

GP = GPIOProcessor()

try:
    Pin27 = GP.getPin27()
    Pin27.out()

    Pin29 = GP.getPin29()
    Pin29.input()	

    Pin27.high()

finally:
    GP.cleanup()
