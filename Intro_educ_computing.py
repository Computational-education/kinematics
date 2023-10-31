import numpy as _np
import matplotlib.pyplot as _plt 
import scipy.integrate as _scyint
import scipy.special as _special


class Basic_kinematics():

    def __init__(self, learning_level, v_0=None, s_0=None, time=None):

        if v_0 is None:
            v0 = 10 # in I.S. [m/s]
        if s_0 is None:
            s0 = 0 # in I.S. [m]
        if time is None:
            t = _np.linspace(0, 50, 5000) 
        
        if 'infantil' in learning_level:
            self._learn = 'infantil'
        elif 'fundamental' in learning_level:
            self._learn = 'fundamental'
        elif 'médio' in learning_level:
            self._learn = 'médio'
        else:
            self._learn = 'graduação'

        if self._learn == 'graduação':
            # _b when the force is proportional to velocity, this parameter is the drag_coefficient. It is well known as damping coefficient
            # when studying the harmonic damped oscilator
            self._b = 0.1 # in Internatinal System of Units [kg/s]
        else:
            # Forces proportional to velocity aren't a familiar theme for kids and undergraduated studants, so take it ease :),
            # one day they will know about it, if it is their interest
            self._b = 0

        self._v_0 = v0
        self._s_0 = s0
        self._a = 0 # taking acceleration to be zero so the moviment of the body is an Uniform Motion
        self._theta = None # this angle must be the angle of the oblique throwing
        self._gravity = 10 # approximatly, [m/s^2] in International System of Units
        self._time = t
        self._space = _np.linspace(0,100, 10000) # this parameter is important when velocity can be described in terms of the space
        self._frequency = 10000 # wheel's rotation
        self._light_speed =  299792458 # in International System of Units [m/s]
        self._sound_speed = 343 # in International System of Units [m/s]
        self.frequency = None
        self._reverb_time = 0.1 # [s]
        self._mass = 10 # kg
        self._force = None

    @property
    def v_0(self):
        return self._v_0
    
    @v_0.setter
    def v_0(self, new_value):
        self._v_0 = new_value
    
    @property
    def s_0(self):
        return self._s_0
    
    @s_0.setter
    def v_0(self, new_value):
        self._s_0 = new_value

    @property
    def acceleration(self):
        return self._a
    
    @acceleration.setter
    def acceleration(self, new_value):
        self._a = new_value
    
    @property
    def theta(self):
        if self._theta is None:
            self._theta = _np.pi/4 # If u ask me why I chose this angle, keep in mind that it keep an important property in an oblique throw.
                                   # Hint: compare the distance traveled by a particle thrown by an angle of pi/6 and pi/3
        return self._theta
    
    @theta.setter
    def theta(self, new_value):
        self._theta = new_value
    
    @property
    def gravity(self):
        return self._gravity
    
    @gravity.setter
    def gravity(self, new_value): # user could set the value of the gravity if is desired travel to another planet :O
        self._theta = new_value
    
    @property
    def drag_coef(self):
        return self._b
    
    @drag_coef.setter
    def drag_coef(self, new_value):
        if 'graduation' in self._learn:
            self._b = new_value
        else:
            print('O educador poderá te auxiliar a obter informações sobre este assunto! \n Não tenha medo de perguntar, divirta-se!')
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, time_range, nsteps):
        t = _np.linspace(0,time_range, nsteps)
        self._time = t

    @property
    def light_speed(self):
        return self._light_speed
    
    @property
    def sound_speed(self):
        return self._sound_speed
    
    @property
    def space(self):
        return self._space
    
    @space.setter
    def space(self, new_intial_bound,new_space, nsteps):
        spc = _np.linspace(new_intial_bound, new_space, nsteps)
        self._space = spc

    @property
    def mass(self):
        return self._mass
    
    @mass.setter
    def mass(self, new_value):
        self._mass = new_value # forneça a massa em unidades do SI

    @property
    def force(self):
        if self._force is None:
            self._force = self._mass * self._a
        return self._force
    
    @force.setter
    def force(self, new_value):
        self._force = new_value

    def seno(self):
        return 100* _np.sin(self._time)
    
    def exp(self):
        return 10*_np.exp(self.time)
    
    def quadratica(self, posicao_0, speed_0, acceleration_0):
        s_position = posicao_0
        s_position += speed_0 * self._time
        s_position += 1/2 * acceleration_0 * self._time ** 2
        
        return s_position
    
    def line(self,  posicao_0, speed_0):
        s_position = posicao_0
        s_position+= speed_0 * self._time

        return s_position

    def cos(self):
        return 100*_np.cos(self._time)
    
    def tan(self):
        return _np.tan(self._time)
    
    def bessel(self, n):
        return 100*_special.jn(n, self._time)

    def graficos_para_EM(self, acceleration_0, speed_0, posicao_0):

        # como este é um método estático não é necessário criar estruturas 
        # de decisão para diferenciar as diferentes formas de movimento

        fig, (a1,a2,a3) = _plt.subplots(nrows=1, ncols=3, figsize=(10,5))
        time = self._time

        s_position = posicao_0
        s_position += speed_0 * time
        s_position += 1/2 * acceleration_0 * time ** 2

        speed = speed_0
        speed += acceleration_0 * time

        acceleration = acceleration_0 * _np.ones(time.size)

        a1.set_title(r'Posição $\times$ tempo', fontsize=16)
        a1.set_ylabel(r'S [$m$]', fontsize=14)
        a1.set_xlabel(r'tempo [$s$]', fontsize=14)
        a1.grid(True, alpha=0.5, ls='--', color='k')
        a1.tick_params(axis='both', labelsize=14)

        a2.set_title(r'Velocidade $\times$ tempo', fontsize=16)
        a2.set_ylabel(r'v [$m/s$]', fontsize=14)
        a2.set_xlabel(r'tempo [$s$]', fontsize=14)
        a2.grid(True, alpha=0.5, ls='--', color='k')
        a2.tick_params(axis='both', labelsize=14)

        a3.set_title(r'Aceleração $\times$ tempo', fontsize=16)
        a3.set_ylabel(r'a [$m/s^{2}$]', fontsize=14)
        a3.set_xlabel(r'tempo [$s$]', fontsize=14)
        a3.grid(True, alpha=0.5, ls='--', color='k')
        a3.tick_params(axis='both', labelsize=14)

        a1.plot(time, s_position, label=r'$s(t)$')
        a1.legend(fontsize=14)
        a2.plot(time, speed, label=r'$v(t)$')
        a2.legend(fontsize=14)
        a3.plot(time, acceleration, label=r'$a(t)$')
        a3.legend(fontsize=14)

        fig.tight_layout()

    
    def creat_dict(self):
        # If the student desire to knows what happens if other functions are the input for the graphic's plot 
        dic = {}

        dic['seno'] = self.seno()
        dic['exp'] = self.exp()
        dic['quadratico'] = self.quadratica(-6,-1,2)
        dic['reta'] = self.line(5, 2)
        dic['tangente'] = self.tan()
        dic['cosseno'] = self.cos()
        dic['bessel'] = self.bessel(0)

        return dic

    def plotar_intersec(self, name1, name2):

        dic = self.creat_dict()

        array_pos_1 = dic['{}'.format(name1)]
        array_pos_2 = dic['{}'.format(name2)]

        fig, ax = _plt.subplots(figsize=(10,5))
        time = self._time

        ax.set_title('Intersecção entre as posições de duas partículas', fontsize=16)

        ax.plot(time, array_pos_1, label=r'$s_{1}$')
        ax.plot(time, array_pos_2, label=r'$s_{2}$')

        ax.set_ylabel(r'posição das partículas [m]', fontsize=14)
        ax.set_xlabel(r'tempo [s]', fontsize=14)
        ax.grid(True, alpha=0.5, ls='--', color='k')
        ax.xaxis.grid(False)
        ax.tick_params(axis='both', labelsize=12)
        ax.legend(loc='best')

        fig.tight_layout()



    

