export interface ICharm {
  name: string;
  store_front: {
    icons: string[];
    "display-name": string;
    "deployable-on": string[];
  };
  result: {
    publisher: {
      "display-name": string;
    };
  };
  "default-release": {
    channel: {
      risk: string;
      name: string;
      track: string;
    };
  };
}
