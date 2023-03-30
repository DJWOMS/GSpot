import List from 'components/List'
import { ListWrapper } from 'components/List/List'
import Section from 'components/Section'
import styles from './OtherGames.module.scss'

const GameItem = () => <List coverImg={'https://loremflickr.com/240/320'} price={1.99} title={'The Evil Within: The Assignment'} sale={4.99} />

const OtherGames = () => {
  return (
    <div className={styles.sections}>
      <Section title="Game cards">
        <ListWrapper>
          <GameItem key={1} />
          <GameItem key={2} />
          <GameItem key={3} />
        </ListWrapper>
      </Section>

      <Section title="Gift cards">
        <ListWrapper>
          <GameItem key={1} />
          <GameItem key={2} />
          <GameItem key={3} />
        </ListWrapper>
      </Section>

      <Section title="Subscription cards">
        <ListWrapper>
          <GameItem key={1} />
          <GameItem key={2} />
          <GameItem key={3} />
        </ListWrapper>
      </Section>
    </div>
  )
}

export { OtherGames }
