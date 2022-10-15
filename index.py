from sympy import *
import streamlit as st
st.title('求Omega')
'''
## 输入 theta 、beta、P 的值
'''
Theta1 = st.number_input('Theta 1')
Beta1 = st.number_input('Beta 1')
Theta2 = st.number_input('Theta 2')
Beta2 = st.number_input('Beta 2')
Theta3 = st.number_input('Theta 3')
Beta3 = st.number_input('Beta 3')
P=st.number_input('P')
w1,w2,w3 = symbols('omega_1 omega_2 omega_3')
theta1,theta2,theta3= symbols('theta1 theta2 theta3')
beta1,beta2,beta3 = symbols('beta_1 beta_2 beta_3')
theta1 = Theta1
theta2 = Theta2
theta3 = Theta3
beta1 = Beta1
beta2 = Beta2
beta3 = Beta3
p = symbols('P')
p = P
div1 = 1/(theta1+beta1*w1)
div2 = 1/(theta2+beta2*w2)
div3 = 1/(theta3+beta3*w3)
eq1 = Eq(((-2-div1)*w1+2*w2-p),0)
eq2 = Eq(((-2-div2)*w2+w1+w3),0)
eq3 = Eq(((-2-div3)*w3+2*w2),0)
def computed():
  res = solve((eq1,eq2,eq3),(w1,w2,w3))
  res
st.button('计算',on_click=computed)
