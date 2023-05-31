import example

tire = example.create_random_tire()
print(f'Tire pressure: {tire.pressure:.2f}')
print(f'Tire material: {tire.material}')
print(f'Tire size: {tire.size.width:.2f} width, {tire.size.height:.2f} height')
print(f"The tire have an aspect ratio of {example.wheel_size_aspect(tire.size.width, tire.size.height):.2f}")

example.func_with_no_return()
