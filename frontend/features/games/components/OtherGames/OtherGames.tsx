import List from 'components/List'
import { ListWrapper } from 'components/List/List'
import Section from 'components/Section'
import styles from './OtherGames.module.scss'

const GameItem = () => <List />

const OtherGames = () => {
  return (
    <div className={styles.sections}>
      <Section title="Gaming cards">
        <ListWrapper>
          <GameItem />
          <GameItem />
          <GameItem />
        </ListWrapper>
      </Section>

      <Section title="Gift cards">
        <ListWrapper>
          <GameItem />
          <GameItem />
          <GameItem />
        </ListWrapper>
      </Section>

      <Section title="Subscription cards">
        <ListWrapper>
          <GameItem />
          <GameItem />
          <GameItem />
        </ListWrapper>
      </Section>
    </div>
  )
}

export { OtherGames }
