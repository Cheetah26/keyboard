    return {
            'brightness': self.brightness,
            'brightness_step': self.brightness_step,
            'brightness_limit': self.brightness_limit,
        }

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, sandbox):
        '''Light up every single led once for 200 ms'''
        for i in range(self._led_count + 2):
            if i < self._led_count:
                self._leds[i].duty_cycle = int(self.brightness / 100 * 65535)
            i_off = i - 2
            if i_off >= 0 and i_off < self._led_count:
                self._leds[i_off].duty_cycle = int(0)
            time.s