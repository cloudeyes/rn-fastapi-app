import React, { memo, useState } from 'react';
import { StyleSheet, Text, TextInput as NativeInput } from 'react-native';
import { Input, Item, Label } from 'native-base';
import { theme } from '../core/theme';

type Props = React.ComponentProps<typeof NativeInput> & {
  error?: boolean;
  label?: string;
  errorText?: string;
};

const TextInput = ({ label, errorText, ...props }: Props) => {
  const [input, setInput] = useState(null) as [any, any];
  return (
    <>
      <Item
        floatingLabel
        style={styles.container}
        onPress={() => input && input._root.focus()}
      >
        <Label style={styles.label}>{label}</Label>
        <Input
          getRef={setInput as any}
          style={styles.input}
          selectionColor={theme.colors.primary}
          {...props}
        />
      </Item>
      {errorText ? <Text style={styles.error}>{errorText}</Text> : null}
    </>
  );
};

const styles = StyleSheet.create({
  container: {
    marginVertical: 12,
    width: '100%',
  },
  input: {
    width: '100%',
    color: theme.colors.secondary,
  },
  label: {
    color: theme.colors.secondary,
    paddingLeft: 4,
    opacity: 0.8,
    flex: 1,
    alignSelf: 'stretch',
  },
  error: {
    width: '100%',
    fontSize: 14,
    color: theme.colors.error,
    paddingHorizontal: 4,
  },
});

export default memo(TextInput);
