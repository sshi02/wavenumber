# wavenumber.py
CLI tool for quick evaluation of wavenumber, wavelength, and depth to wavelength ratio.  
A recursive Newton-Raphson function and shallow-water approximation are used to calculate and output the above.

### arguments
- `-h` water depth
- `-T` period
- `-w` angular frequency
- `-e` error
### usage
At minimum, the tool needs depth (`-h`) and either period (`-T`) or angular frequency (`-w`) to run.  
The error (`-e`) is an optional argument, used for establishing the desired margin between guesses from the Newton-Raphson method. By default the error is e-5.

##### example 1
`python3 wavenumber.py -h 5 -T 10`

#### example 2
`python3 wavenumber.py -w 0.63 -e 0.01 -h 8 `

#### example input --> output
![image](https://user-images.githubusercontent.com/86270509/185037217-2fd0ded3-fd7a-441d-ab7d-7b1eb98f1f05.png)
