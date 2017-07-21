import { MkpollPage } from './app.po';

describe('mkpoll App', () => {
  let page: MkpollPage;

  beforeEach(() => {
    page = new MkpollPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});
