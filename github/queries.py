RATE_LIMIT = """
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
"""

ISSUES_QUERY = """
query($owner: String!, $name: String!, $issues_per_page: Int!, $first_reactions: Int!, $first_comments: Int!, $page_after: String) {
  repository(owner: $owner, name: $name) {
    %s(first: $issues_per_page, orderBy: {field: CREATED_AT, direction: DESC}, after: $page_after) {
      totalCount
      pageInfo {
        endCursor
        startCursor
      }
      nodes {
        id
        number
        url
        title
        body
        bodyText
        bodyHTML
        author {
          login
          ... on User {
            email
            avatarUrl
            url
          }
        }
        authorAssociation
        closed
        closedAt
        createdAt
        state
        updatedAt
        lastEditedAt
        editor {
          login
          avatarUrl
          url
        }
        activeLockReason
        timelineItems(last: 1) {
          nodes {
            __typename
            ... on IssueComment {
              updatedAt
              author {
                login
                avatarUrl
                url
              }
            }
            ... on ClosedEvent {
              createdAt
              actor {
                login
              }
            }
            ... on ReopenedEvent {
              createdAt
              actor {
                login
              }
            }
            ... on RenamedTitleEvent {
              currentTitle
              previousTitle
              createdAt
              actor {
                login
              }
            }
          }
        }
        labels(first: 5) {
          nodes {
            name
            color
            description
          }
        }
        milestone {
          title
          state
          description
          dueOn
        }
        assignees(first: 5) {
          nodes {
            login
            avatarUrl
            url
          }
        }
        reactions(first: $first_reactions) {
          totalCount
          nodes {
            user {
              login
              email
              avatarUrl
              url
            }
            content
            createdAt
          }
        }
        comments(first: $first_comments) {
          totalCount
          nodes {
            id
            url
            body
            author {avatarUrl login url}
            authorAssociation
            createdAt
            reactionGroups {content createdAt}
          }
        }
      }
    }
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""



PR_QUERY = """
query($owner: String!, $name: String!, $issues_per_page: Int!, $first_reactions: Int!, $first_comments: Int!, $page_after: String) {
  repository(owner: $owner, name: $name) {
    %s(first: $issues_per_page, orderBy: {field: CREATED_AT, direction: DESC}, after: $page_after) {
      totalCount
      pageInfo {
        endCursor
        startCursor
      }
      nodes {
        number
        url
        title
        body
        author {
          login
          ... on User {
            email
          }
          avatarUrl
          url
        }
        authorAssociation
        closed
        closedAt
        createdAt
        state
        updatedAt
        merged
        mergedAt
        mergedBy {
          login
          avatarUrl
          url
        }
        isCrossRepository
        headRepository {
          nameWithOwner
        }
        baseRepository {
          nameWithOwner
        }
        reactions(first: $first_reactions) {
          totalCount
          nodes {
            user {
              login
              email
              avatarUrl
              url
            }
            content
            createdAt
          }
        }
        reviews(first: 10) {
          totalCount
          nodes {
            author {
              login
              ... on User {
                  email
            }
            }
            url
            authorAssociation
            body
            comments(first: 10) {
              nodes {
                author {
                  login
                  ... on User {
                   email
                }
                }
                url
                body
                reactions(first: 10) {
                  totalCount
                  pageInfo {
                    endCursor
                    hasNextPage
                  }
                  nodes {
                    content
                    user {
                      email
                      login
                    }
                  }
                }
              }
            }
          }
        }
        comments(first: $first_comments) {
          totalCount
          nodes {
            id
            url
            body
            author {avatarUrl login url}
            authorAssociation
            createdAt
            reactionGroups {content createdAt}
            # reactions(first: 0) {
            #   totalCount
            #   nodes {
            #     # id
            #     user {login avatarUrl url}
            #     content
            #     createdAt
            #   }
            # }
          }
        }
      }
    }
  }
  rateLimit {
    limit
    cost
    remaining
    resetAt
  }
}
"""
# queries.py

STARGAZERS_QUERY = """
query($owner: String!, $name: String!, $stargazers_per_page: Int!, $page_after: String) {
  repository(owner: $owner, name: $name) {
    stargazers(first: $stargazers_per_page, after: $page_after) {
      totalCount
      pageInfo {
        endCursor
        hasNextPage
      }
      nodes {
        id
        login
              ... on User {
                  email
            }
        name
        email
        url
        createdAt
      }
    }
  }
}
"""


COMMENT_REACTIONS_QUERY = """
node_%s: node(id:"%s") {
     ... on IssueComment {
      id
      reactions(first: 100) {
        totalCount
        nodes {
            user {login avatarUrl url}
            content
            createdAt
          }
      }
    }
  }
"""
