export type Navigation = {
  navigate: (scene: string, params: { [key: string]: any } = undefined) => void;
  getParam(key: string): any;
};
