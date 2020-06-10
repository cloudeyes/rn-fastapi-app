import React, { memo } from 'react';

import Background from '../components/Background';
import Logo from '../components/Logo';
import Header from '../components/Header';
import Button from '../components/Button';
import Paragraph from '../components/Paragraph';
import { Navigation } from '../types';

type Props = {
  navigation: Navigation;
};

const HomeScreen = ({ navigation }: Props) => {
  fetch('http://localhost:8000/hello').then((res) => {
    console.log('res:', res);
    if (res.status === 401) {
      navigation.navigate('LoginScreen');
    }
  });

  return (
    <Background>
      <Logo />
      <Header>Login Template</Header>

      <Paragraph>
        The easiest way to start with your amazing application.
      </Paragraph>
      <Button
        title="Login"
        onPress={() => navigation.navigate('LoginScreen')}
      />
      <Button
        bordered
        title="Sign Up"
        onPress={() => navigation.navigate('RegisterScreen')}
      />
    </Background>
  );
};

export default memo(HomeScreen);
