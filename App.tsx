import * as React from 'react';
import { StatusBar, View, Text } from 'react-native';
import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import CardStackStyleInterpolator from 'react-navigation-stack/src/views/StackView/StackViewStyleInterpolator';

import { AppLoading } from 'expo';
import * as Font from 'expo-font';
import { Ionicons } from '@expo/vector-icons';

StatusBar.setBarStyle('light-content');

import {
  HomeScreen,
  LoginScreen,
  RegisterScreen,
  ForgotPasswordScreen,
  Dashboard,
} from './src/screens';
import { useState } from 'react';
import { Container } from 'native-base';

const Router = createStackNavigator(
  {
    HomeScreen,
    LoginScreen,
    RegisterScreen,
    ForgotPasswordScreen,
    Dashboard,
  },
  {
    initialRouteName: 'HomeScreen',
    headerMode: 'none',
    transitionConfig: () => ({
      screenInterpolator: CardStackStyleInterpolator.forHorizontal,
    }),
  }
);

const App = createAppContainer(Router);

export default function Main() {
  const [isReady, setIsReady] = useState(false);

  Font.loadAsync({
    Roboto: require('native-base/Fonts/Roboto.ttf'),
    Roboto_medium: require('native-base/Fonts/Roboto_medium.ttf'),
    ...Ionicons.font,
  }).then(() => {
    setIsReady(true);
  });

  return !isReady ? <AppLoading /> : <App />;
}
