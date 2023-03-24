import List from 'components/List'
import Section from 'components/Section'
import { ListWrapper } from 'components/List/List'

const GameItem = () => <List coverImg={'https://picsum.photos/240/340'} price={1.99} title={'The Evil Within: The Assignment'} sale={4.99} />

const OtherGames = () => {
  const children = (
    <ListWrapper>
      <GameItem key={1} />
      <GameItem key={2} />
      <GameItem key={3} />
    </ListWrapper>
  )

  return (
    <Section
      items={[
        {
          title: 'Gaming Cards',
          children,
        },
        {
          title: 'Gift Cards',
          children,
        },
        {
          title: 'Subscriptions',
          children,
        },
      ]}
    />
  )
}

export default OtherGames
