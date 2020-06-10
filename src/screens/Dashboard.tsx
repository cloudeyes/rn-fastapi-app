import React, { memo, useState } from 'react';
import Background from '../components/Background';
import Logo from '../components/Logo';
import Header from '../components/Header';
import Paragraph from '../components/Paragraph';
import Button from '../components/Button';
import { Navigation } from '../types';

type Props = {
  route: { params: any };
  navigation: Navigation;
};

const Dashboard = ({ navigation }: Props) => {
  const [message, setMessage] = useState('loading...');
  const token = navigation.getParam('token');
  if (token) {
    console.log('token:', token);
    fetch('http://localhost:8000/hello', {
      headers: new Headers({
        Authorization: 'Bearer ' + token,
        'Content-Type': 'application/x-www-form-urlencoded',
      }),
    }).then((res: any) => {
      res.json().then((data: any) => {
        setMessage(JSON.stringify(data));
      });
    });
  }

  return (
    <Background>
      <Logo />
      <Header>Let’s start</Header>
      <Paragraph>{message}</Paragraph>
      <Button
        title="Logout"
        bordered
        onPress={() => navigation.navigate('HomeScreen')}
      />
    </Background>
  );
};

export default memo(Dashboard);
